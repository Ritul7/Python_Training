# Main Markings of DAY 1 tasks

## 1. Client Server Architecture
- Client(ex: Browser) sends the req to Server to get or post some data.
- Server(ex: Web Browser) executes all the business logic and sends the response back to the client.

## 2. How does the Web Works?
- Browser sends the input data to DNS
- DNS converts the domain names into their IP Address, and send it back to browser
- Browser then sends the HTTP/HTTPS requests to the server
- Server sends the response back to browser in form of the files

## 3. HTTP Methods and Status Codes?

### 1. Safe HTTP Methods:
- Read only operations ("GET"(for requesting data, no body demanded), "HEAD"(neither req nor res has body, it is only for requesting metadata), "OPTIONS")
- "GET" and "HEAD" are only cacheable HTTP methods. 
- GET, HEAD, OPTIONS

### 2. Idempotent HTTP Methods:
- If intended effect of a single request on the server is same as the effect of multiple requests.
- "PUT"(Updating complete resource),"DELETE"(Delete the specified resource) are idempotent
- All safe methods are idempotent.
- GET, HEAD, OPTIONS, PUT, DELETE

### Status Codes

They are like indications of response messages of the client's request.

- 200 (OK): CLient's request was Successfull.
- 201 (Created): New resource has created.

- Redirection
- 300 (Multiple Choices): This req have multiple responses, and choose one of them.

- CLient Error
- 400 (Bad request): Incorrect syntax of the req
- 401 (Unauthorized): User not authorized
- 403 (Forbidden): Client doesn't have the access tot he content, but unlike 401, client's identity is known here.
- 404 (Not found): Page not found.

- Server Error
- 500 (Internal Server Error)

## 4. REST APIs Fundamentals

- Uses Standard HTTP Methods for communication between client and server
- APIs should be written using standard REST API methods
- Should properly state the status of response from server by status codes

## 5. HTTPS Importance

- Encrypts the data (login cred, password)
- Authenticates the website's identity using SSL/TLS certificate
- Prevent attacks and improves SEO
- While accessing any website, if the website have a SSL/TLS certificate, it send it to the browser along with the server's public key, just to prove the validation of the website and tell who the owner is.

## 6. API Versioning

- Giving different versions to an API so that it works for old users as well
- WHY? To add new features without breaking

