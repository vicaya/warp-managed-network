Cloudflare WARP Managed Network Helper
======================================

## Get started
```
python3 warp-local-network-id.py <port> <cert-prefix>
```

See [the Cloudflare
doc](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/configure-warp/managed-networks/)
for how to generate unique TLS cert/key for each network

## Run as a service

Put certificate and key in `/etc/warp-local-network/<prefix>`
and change the `warp-local-network-id.service` to reflect the `<prefix>`
(the included example is `home`)

```
sudo install warp-local-network-id.service /etc/systemd/system
sudo systemctl enable warp-local-network-id
sudo systemctl start warp-local-network-id
```
