import urllib.request
import zipfile
import json

release = "0.552.0"
url = "https://github.com/lucide-icons/lucide/releases/download/{}/lucide-font-{}.zip".format(
    release, release
)


def main():
    zip_path, _ = urllib.request.urlretrieve(url)
    with open("lib-map.typ", "w") as f:
        f.write("//GENERATED FILE\n")
        f.write("#let lucide-icon-map = (\n")
        with zipfile.ZipFile(zip_path, "r") as z:
            with z.open("lucide-font/info.json") as file:
                d = json.load(file)
                for name, values in d.items():
                    f.write(
                        '  "{}": "\\u{{{}}}",\n'.format(
                            name, values["encodedCode"].replace("\\", "")
                        )
                    )
        f.write(")\n")


if __name__ == "__main__":
    main()
