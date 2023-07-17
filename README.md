# TessiePy

Python wrapper for the [Tessie](https://tessie.com) API.

## Usage

Initialize `TessieClient` with your Tessie API key. All<sup>*</sup> Tessie API endpoints are supported, and organized according to the Tessie API docuemntation.

```py
from tessiepy import TessieClient

client = TessieClient("YOUR_API_KEY")

client.lights.flash()
```

<sup>* The `/vin/map` endpoint is not supported as it returns image/png data.</sup>

## Disclaimer

I only own a Model 3, so some features exclusive to other Tesla models such as Biohazard Mode and sunroof opening/closing have not been tested. If you own one of these vehicles and are able to confirm they work correctly, please open an issue!

## License

Licensed under the [MIT License](LICENSE.md).