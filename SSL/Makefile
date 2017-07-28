SSL_CRT_PATH := /xxx/ssl.crt/
SSL_KEY_PATH := /xxx/ssl.key/
UI_SCRIPT_PATH := /xxx/S99ADMINUI

# configure file /etc/pki/tls/openssl.cnf
.PHONY: ca_key ca_crt server_key server_csr server_crt print clean
all: ca_key ca_crt server_key server_csr server_crt 

# RSA private key to produce ca.key(RSA Key Length: 2048)
# Use des3 to encrypt the ca.key again, we need to input a string as pass phrase
ca_key:
	openssl genrsa -des3 -out ca.key 2048

# certificate (Valid Period：20 Years) to produce ca.crt
ca_crt:
	openssl req -new -x509 -days 7305 -key ca.key -out ca.crt

# Create intermediate RSA private key server.key(RSA Key Length: 2048)
server_key:
	openssl genrsa -out server.key 2048

# Create certificate request file server.csr
server_csr:
	openssl req -new -key server.key -out server.csr

# Create intermediate certificate server.crt from certificate ca.crt 
# and using it's private key ca.key the valid period is 20 Years extfile is 
# to configure "subjectAltName". v3.ext content refer Note 1).
server_crt:
	openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key -days 7305 -extfile v3.ext

install:
	cp server.crt $(SSL_CRT_PATH)
	cp server.key $(SSL_KEY_PATH)
	$(UI_SCRIPT_PATH) stop
	$(UI_SCRIPT_PATH) start

# print the certificate in text form
print:
	openssl x509 -in ca.crt -text
clean:
	rm -rf ca.key ca.crt server.csr server.key server.crt
 
# Note:
#   1) file v3.ext content
#   ```
#   authorityKeyIdentifier=keyid,issuer
#   basicConstraints=CA:FALSE
#   keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
#   subjectAltName = @alt_names
#
#   [alt_names]
#   DNS.1 = xxx
#   ```
