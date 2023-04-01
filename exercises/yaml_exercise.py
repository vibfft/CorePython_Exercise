import yaml

f = None
try:
    f = open('config.yaml', 'r')
    prime_service = yaml.safe_load(f)
    print(f"service: {prime_service}")

    print(f"url: {prime_service['rest']['url']}")
except Exception as e:
    print(e)

finally:
    f.close()
