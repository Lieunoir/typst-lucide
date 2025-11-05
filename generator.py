import urllib.request
import zipfile

release = "0.552.0"
# shah = "sha256:9bb6a877788928de7c6d0711ead07fc3eb162611059ce72badefa5e670b4974f"
url = "https://github.com/lucide-icons/lucide/releases/download/{}/lucide-icons-{}.zip".format(
    release, release
)


def main():
    zip_path, _ = urllib.request.urlretrieve(url)
    with open("lib-map.typ", "w") as f:
        f.write("//GENERATED FILE\n")
        f.write("#let lucide-icon-map = (\n")
        with zipfile.ZipFile(zip_path, "r") as z:
            for full_path in z.namelist():
                root, path = full_path.split("/")
                if path.endswith(".svg"):
                    name, extension = path.split(".")
                    with z.open(full_path) as file:
                        f.write('  "{}": "'.format(name))
                        text = file.read().decode()
                        start = text.find('>')+1
                        end = text.rfind('<')
                        for line in text[start:end].splitlines():
                            f.write(line.strip().replace('"', '\\"'))
                        f.write('",\n')
        f.write(")\n")


if __name__ == "__main__":
    main()
