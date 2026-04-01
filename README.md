This repo provides a template for running python application in a VPN-enabled docker container. Specifically, it is running on MacOS + ProtonVPN (free tier) + Orbstack.

Note that only the docker container will have VPN enabled. That doesn't affect your local machine and you can use services on your local machine without VPN.

# Preparation
## VPN-related
1. Download WireGuard config file from ProtonVPN. Details see [here](https://protonvpn.com/support/wireguard-configurations?srsltid=AfmBOoqfbUugNE8sZvYbYAWAGCWi-y-zZeRCNiC0tdVbh822L6G0li-h). Note that you should not attach the `.conf` file you get to this project/you should gitignore it.
2. Set `.env` by copying needed credentials from the above `.conf` file.

## Application-related
1. Use `python -m venv .venv` to create a new virtual env, then use `source .venv/bin/activate` to activate it.
2. Add your application's env variables to `.env.app`.
3. After writing your python scripts, do `pip freeze > requirements.txt`.
4. Update Dockerfile as needed.

## Docker-related
1. Open Orbstack.
2. Update `docker-compose.yml` and `.dockerignore` as needed.
3. To create and start your docker container, do `docker compose up --build`.
4. If there is any update in the `docker-compose.yml` or `Dockerfile`, you should first do `docker compose down` then do step 1 again to update the files.
5. If there is any update in your python scripts, no need to perform step 2 and can directly perform step 1 again.