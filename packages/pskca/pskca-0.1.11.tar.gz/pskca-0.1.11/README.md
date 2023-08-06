# Pre-shared key-based certificate authority and requestor

This package implements a protocol for certificate issuance that two parties
(a server, the CA -- and a client, the requestor) can use to negotiate the
issuance of certificates valid from the perspective of the CA.  The only
prerequisites for a successful certificate issuance are:

1. There is a cleartext communication channel between the two parties.
2. Both parties already have a PSK they both trust (generated, perhaps
   with the blindecdh Python module, and then subsequently verified
   by both parties).

The purpose of this is to establish enduring trust between server and client.

After successful untampered and verified key exchange between two parties
(the server and the client), both have a shared secret they can use to encrypt
and decrypt traffic.  This is useful, but the key is not enough — the modern
goal of communications cryptography is to arrive at mutually authenticated TLS
between the peers, so that the peers can then continue in a fully symmetrically
authenticated manner (e.g. via mTLS or gRPC).

The package contains two main parts:

1. a certificate authority (CA) capable of issuing certificates to authorized
   entities,
2. a certificate requestor to negotiate certificate issuance requests with the
   certificate authority.

Authentication for certificate issuance is predicated on both sides (the CA
and the requestor) holding a pre-shared key (which can be negotiated via ECDH
using the [blindecdh package](https://github.com/Rudd-O/blindecdh) and then
authorized using the
[shortauthstrings package](https://github.com/Rudd-O/shortauthstrings)).

A set of utility functions and objects are also provided to simplify use of
this package.

Here is some sample code:

```
import os, pskca

client_id = "xxx"
ca_cert, ca_key = pskca.create_certificate_and_key(ca=True)
client_csr, client_key = pskca.create_certificate_signing_request()
psk = os.urandom(32)

C = pskca.CA(ca_cert, ca_key)
C.add_psk(client_id, psk)
R = pskca.Requestor(psk)
payload = R.encrypt_csr(client_csr)
# If you were sending the encrypted payload over the wire, you'd then
# call .to_bytes() on the object resulting from encrypt_csr() call.
_, __, enc_client_cert, enc_cert_chain = C.issue_certificate(client_id, payload)

# If you received enc_client_cert and enc_cert_chain over the wire,
# they'd be bytes, so you'd create the respective objects thus:
# enc_client_cert = pskca.EncryptedClientCertificate(enc_client_cert)
# enc_cert_chain = pskca.EncryptedCertificateChain(enc_cert_chain)
client_cert, enc_cert_chain = R.decrypt_reply(enc_client_cert, enc_cert_chain)

print("Client certificate obtained: %s" % client_cert)
print("Root of trust certificate obtained: %s" % cert_chain)
print("CA certificate should be valid according to root of trust: %s" % ca_cert)

# Client certificate obtained: <Certificate(subject=<Name(CN=projects)>, ...)>
# Root of trust certificate obtained: [<Certificate(subject=<Name(C=XX,...)>...]
# CA certificate should be valid according to root of trust: <Certificate(subject=<Name(C=XX...)>
```

You'll find more developer and implementation documentation in the
[module](https://github.com/Rudd-O/pskca/blob/master/src/pskca/__init__.py).

This package is distributed under the GNU Lesser General Public License v2.1.
For relicensing, contact the package author.
