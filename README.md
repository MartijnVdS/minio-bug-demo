# Test case 

Test case for https://github.com/minio/minio/issues/9266

To run the following commands (assumes "docker-compose", "mkcert" and "mc" are installed):

1. Create the certificates: `CAROOT=$(pwd)/certs mkcert -cert-file certs/dev.crt -key-file certs/dev.key *.127.0.0.1.xip.io`
2. Start the test environment: `docker-compose up`
3. Copy the root CA certificate so `mc` can find/use it: `cp certs/rootCA.pem ~/.mc/certs/CAs/rootCA.pem`
4. Add local minio to `mc` configuration: `mc config host add test https://minio.127.0.0.1.xip.io/ DevAccessKey DevSecretKey`
5. Create a bucket: `mc mb test/bucket`
6. Add event callback: `mc event add test/bucket arn:minio:sqs::_:webhook`
7. Copy a file: `mc cp docker-compose.yml test/bucket`

Notice in step 7, minio logs a failure to call the webhook, even though the rootCA.pem
CA certificate is mounted in the /root/.minio/certs/CAs/ directory inside the minio container.

Calling the webhook POST manually with curl shows that the basic setup works:
* `curl -XPOST -d "Hello" --cacert certs/rootCA.pem https://webhook.127.0.0.1.xip.io/webhook`

This logs `Hello` to the `webhook` container logs.