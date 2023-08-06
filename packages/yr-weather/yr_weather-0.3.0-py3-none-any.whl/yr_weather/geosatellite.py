import requests
from requests_cache import CachedSession
from typing import Optional, Literal, Union, get_args
from .base import BaseClient
from datetime import datetime

from .types.geosatellite import SatArea

class Geosatellite(BaseClient):
    """A client for interacting with the Yr Geosatellite API."""
    def __init__(self, headers: Optional[dict] = {}, use_cache: Optional[bool] = True) -> None:
        super().__init__(headers, use_cache)

        self._baseURL += "geosatellite/1.4/"

    def get_image(self,
        area: Optional[SatArea] = "europe",
        img_type: Optional[Literal["infrared", "visible"]] = "infrared",
        time: Optional[str] = None,
        size: Optional[Literal["normal, small"]] = "normal"
    ) -> requests.Response:
        """Get a geosatellite image.
        
        Parameters
        ----------
        area: Optional[:data:`.SatArea`]
            The area for the image. Must be a valid :data:`.SatArea`.
        img_type: Optional[Literal["infrared", "visible"]]
            The image type. Either "infrared" or "visible".
        time: Optional[:class:`str`]
            The time formatted as described in MET.no's documentation.
        size: Optional[Literal["normal, small"]]
            Image resolution. Either "normal" or "small" for thumbnails.
        
        Returns
        -------
        requests.Response
            A Response class enabling saving or futher management of the data received.
        """
        areaArgs = list(get_args(SatArea))
        typeArgs = ["infrared", "visible"]
        sizeArgs = ["normal", "small"]

        if area not in areaArgs:
            raise ValueError(f"The 'area' parameter must be one of the possible SatAreas: {areaArgs}")
        
        if img_type not in typeArgs:
            raise ValueError(f"The 'img_type' parameter must be one of the possible image types: {typeArgs}")

        if size not in sizeArgs:
            raise ValueError(f"The 'size' parameter must be one of the possible sizes: {sizeArgs}")

        URL = self._baseURL + f"?area={area}&type={img_type}&size={size}"

        if time:
            URL += f"&time={time}"
        
        request = requests.get(URL, stream=True)

        if not request.ok:
            raise requests.HTTPError(f"Unsuccessful response received: {request.status_code} {request.reason}.")

        return request
