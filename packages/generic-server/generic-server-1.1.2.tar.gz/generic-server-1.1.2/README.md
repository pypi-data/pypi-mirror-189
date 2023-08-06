# Generic-Server

Python generic TCP/UDP server implementation, with configurable request-response modules (e.g, 'ok', 'reflect', 'json').

**Status:**  Beta\
**Authors:** Carsten König

## Purpose

Sometimes you need a TCP or UDP server that answers with a specific strings to a given request.  For testing different network components in a lab environment, some components in the network might not be available. In order to simulate their presence, Generic-Server answers TCP or UDP string requests using modules either with pre-defined responses or simulated behaviour. 

## Installation

```bash
pip install generic-server
```

## How to use
In order to start a Generic-Server, start the server with the desired config:

```bash
genericserver <protocol> <port> <responder>
```

**protocol**: either TCP or UDP \
**port**: port to listen on \
**responder**: one out of 'ok', 'reflect', 'manual' or 'json'

<ul>

**ok**:         Always sends 'ok' as an answer.\
**reflect**:    Reflects the request string back to the sender.\
**manual**:     Prompts the user to manually enter an answer.\
**json**:       Get answers from a json document. For nested json, a delimiter
            can be chosen (default ':').\
            Example:

```json 
{"test": {
        "a": "1",
        "b": 2
        }
}
```

Request:  `test:a`\
Response: `1`
</ul>

## License
[GNU GPLv3 License](https://choosealicense.com/licenses/gpl-3.0/)

## Author
**Carsten König**

- [GitLab](https://gitlab.com/ck2go "Carsten König")
- [GitHub](https://github.com/ck2go "Carsten König")
- [LinkedIn](https://www.linkedin.com/in/ck2go/ "Carsten König")
- [Website](https://www.carsten-koenig.de "Carsten König")

