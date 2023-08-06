import zipfile
from pathlib import Path
from zipfile import ZipFile

import numpy as np
from connectome import Source, meta
from connectome.interface.nodes import Silent

from .cc359 import open_nii_gz_file
from .internals import checksum, licenses, register


@register(
    body_region='Chest',
    license=licenses.CC0_10,
    link='http://medicalsegmentation.com/covid19/',
    modality='CT',
    prep_data_size=None,  # TODO: should be measured...
    raw_data_size='310M',
    task='COVID-19 segmentation',
)
@checksum('medseg9')
class Medseg9(Source):
    """

    Medseg9 is a public COVID-19 CT segmentation dataset with 9 annotated images.

    Parameters
    ----------
    root : str, Path, optional
        path to the folder containing the raw downloaded archives.
        If not provided, the cache is assumed to be already populated.
    version : str, optional
        the data version. Only has effect if the library was installed from a cloned git repository.

    Notes
    -----
    Data can be downloaded here: http://medicalsegmentation.com/covid19/.

    Then, the folder with raw downloaded data should contain three zip archives with data and masks
    (`rp_im.zip`, `rp_lung_msk.zip`, `rp_msk.zip`).

    Examples
    --------
    >>> # Place the downloaded archives in any folder and pass the path to the constructor:
    >>> ds = Medseg9(root='/path/to/downloaded/data/folder/')
    >>> print(len(ds.ids))
    # 9
    >>> print(ds.image(ds.ids[0]).shape)
    # (630, 630, 45)
    >>> print(ds.covid(ds.ids[0]).shape)
    # (630, 630, 45)

    """

    _root: str = None

    @meta
    def ids(_root: Silent):
        result = set()

        with ZipFile(Path(_root) / 'rp_msk.zip') as zf:
            for zipinfo in zf.infolist():
                if zipinfo.is_dir():
                    continue
                file_stem = Path(zipinfo.filename).stem
                result.add('medseg9_' + file_stem.split('.nii')[0])

        return tuple(sorted(result))

    def _file(i, _root: Silent):
        num_id = i.split('_')[-1]
        return zipfile.Path(Path(_root) / 'rp_im.zip', f'rp_im/{num_id}.nii.gz')

    def image(_file):
        with open_nii_gz_file(_file) as nii_image:
            # most CT/MRI scans are integer-valued, this will help us improve compression rates
            return np.int16(nii_image.get_fdata())

    def affine(_file):
        """The 4x4 matrix that gives the image's spatial orientation."""
        with open_nii_gz_file(_file) as nii_image:
            # most CT/MRI scans are integer-valued, this will help us improve compression rates
            return nii_image.affine

    def voxel_spacing(_file):
        """Returns voxel spacing along axes (x, y, z)."""
        with open_nii_gz_file(_file) as nii_image:
            # most CT/MRI scans are integer-valued, this will help us improve compression rates
            return tuple(nii_image.header['pixdim'][1:4])

    def lungs(_file):
        """Boolean mask. Lungs are not separated."""
        mask_file = zipfile.Path(Path(_file.root.filename).parent / 'rp_lung_msk.zip', f'rp_lung_msk/{_file.name}')
        with open_nii_gz_file(mask_file) as nii_image:
            # most CT/MRI scans are integer-valued, this will help us improve compression rates
            return np.uint8(nii_image.get_fdata())

    def covid(_file):
        """
        int16 mask.
        0 - normal, 1 - ground-glass opacities (матовое стекло), 2 - consolidation (консолидация).
        """
        mask_file = zipfile.Path(Path(_file.root.filename).parent / 'rp_msk.zip', f'rp_msk/{_file.name}')
        with open_nii_gz_file(mask_file) as nii_image:
            # most CT/MRI scans are integer-valued, this will help us improve compression rates
            return np.uint8(nii_image.get_fdata())
