
import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    with open(f"01_Python/multi_processing{name}.jpg", "wb") as f:
        f.write(response.content)

    print(f"Finished Downloading {name}")


if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    pros = []

    for i in range(5):
        p = multiprocessing.Process(
            target=downloadFile,
            args=[url, i]
        )
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

    print("All downloads completed!")