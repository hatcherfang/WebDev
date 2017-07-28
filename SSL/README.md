1. Run command "openssl version"
  OpenSSL 1.0.1e-fips 11 Feb 2013
2. We use openssl to create rootCA and then create intermediate certificate, 
then we use intermediate certificate to configure our apache server.
  1) Create root CA "ca.key, ca.crt"
      # RSA private key to produce ca.key(RSA Key Length: 2048)
      # Use des3 to encrypt the ca.key again, we need to input a string as pass phrase
      `openssl genrsa -des3 -out ca.key 2048` 
      # Produce certificate ca.crt by using private key ca.key (valid Period：20 Years)
      `openssl req -new -x509 -days 7305 -key ca.key -out ca.crt`
  2) Create intermediate key and certificate "server.key, server.crt" by using root CA
      # Create intermediate RSA private key server.key(RSA Key Length: 2048)
      `openssl genrsa -out server.key 2048`
      # Create certificate request file server.csr
      `openssl req -new -key server.key -out server.csr`
      # Create intermediate certificate server.crt from certificate ca.crt 
      # and using it's private key ca.key the valid period is 20 Years extfile is 
      # to configure "subjectAltName". v3.ext content refer Note 1).
      `openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key -days 7305 -extfile v3.ext`
  3) Configure apache server and its configure file "httpd.conf"
    a) Configure file "httpd.conf"
      ```
      <VirtualHost *:443>
        ServerName 127.0.0.1
        DocumentRoot /opt/xx/UI/adminUI/ROOT
        SSLEngine On
        SSLCertificateFile /opt/xxx/apache/conf/ssl.crt/server.crt
        SSLCertificateKeyFile /opt/xxx/apache/conf/ssl.key/server.key
      ```  
  4) Restart apache server and install ca.crt in client then you can visit the apache server from client,
  client must install the certificate ca.crt or it can not pass the authentication.
           
3. Except step 2, we can also create endpoint certificate directly to configure our apache server so that we don't need install
the certificate in client and we can use ssl directly.
  1) Configure "/etc/pki/tls/openssl.cnf" of openssl as below, we set `basicConstraints = CA:false`, 
    because rootCA can not be the certificate of apache server, we set basicConstraints as C:false to create
    endpoint certificate.
   '''
   [ v3_ca ]
   # Extensions for a typical CA
   # PKIX recommendation.
   subjectKeyIdentifier=hash
   authorityKeyIdentifier=keyid:always,issuer
   # This is what PKIX recommends but some broken software chokes on critical
   # extensions.
   #basicConstraints = critical,CA:true
   # So we do this instead.
   basicConstraints = CA:false
   ....
   
   '''
  2) Create endpoint key and certificate
      # RSA private key to produce ca.key(RSA Key Length: 2048)
      # Use des3 to encrypt the ca.key again, we need to input a string as pass phrase
      `openssl genrsa -des3 -out ca.key 2048` 
      # Produce certificate ca.crt by using private key ca.key (valid Period：20 Years)
      `openssl req -new -x509 -days 7305 -key ca.key -out ca.crt`
  3) Configure apache server and its configure file "httpd.conf, httpd-ssl.conf" and add file "ssl-passphrase.sh"
    a) Configure file "httpd.conf"
      ```
      <VirtualHost *:443>
        ServerName 127.0.0.1
        DocumentRoot /opt/xx/UI/adminUI/ROOT
        SSLEngine On
        SSLCertificateFile /opt/xxx/apache/conf/ssl.crt/server.crt
        SSLCertificateKeyFile /opt/xxx/apache/conf/ssl.key/server.key
      ```
    b) Configure file "httpd-ssl.conf"
      '''
      #   Pass Phrase Dialog:
      #   Configure the pass phrase gathering process.
      #   The filtering dialog program (`builtin' is an internal
      #   terminal dialog) has to provide the pass phrase on stdout.
      SSLPassPhraseDialog  exec:/opt/xxx/apache/conf/extra/ssl-passphrase.sh
      '''
    c) New a file "ssl-passphrase.sh" content as below
      '''
      #!/bin/sh
      echo "passphrase-password"
      '''
      chmod +x /opt/bin/ssl-passphrase.sh
      replace "passphrase-password" with pass phrase
    step b), c) to avoid input pass phrase every time when restart apache server.
Note:
  1) file v3.ext content
  ```
  authorityKeyIdentifier=keyid,issuer
  basicConstraints=CA:FALSE
  keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
  subjectAltName = @alt_names

  [alt_names]
  DNS.1 = xxx
  ```
  2) You can refer Makefile to create certificate and primary key
