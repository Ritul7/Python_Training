# DAY-5 Learnings:-

## 1. Password Hashing and Authentication Security

- Password hashing - Process of hashing (converting a plaintext password into a fixed length string of characters) and storing the hashed password instead of storing the plaintext directly in the database
- Hashing - One way process, once plaintext converted into hash, it can not be reverted back. Regardless of input size, the hash will be of fixed length.
- Process: Plaintext + Salt (Unique for every password), the hash is stored in the db along with the salt.

- Encryption - Process of protecting sensitive info by converting plaintext into ciphertext which using an encryption key, and that ciphertext can be converted back into plaintext using decryption key.
- Symmetric Encryption involves a shared sectret key for encyption and decryption purpose.
- Asymmetric Encryption involves public key for encryption and private key for decryption, private key is never shared.

- Authenctiation is the process of verifying an user's identity.
- Access Token is used by the user to get access of secured access without checking-in frequently. SHort - lived only
- Refreah Token - It is used for generating access token and is long-lived.

-: Types of Authentication Security:-

- Single Factor Authentication - Email and password checking only.
- Two-Factor Authentication - Email, password and another entity may be the wireless token or virtual token or OTP. Provide an extra layer of verification.
- Multi-Factor Authentication - It is an extension of Two Factor Authentication, which requires much more fields than in 2FA.
- SS0 - Single Sign-On -> It is an authentication solution that allows users to authenticate to multiple apps and website using single set of credentials. Like logging in a google account gives us the access to gmail, drive, photos etc.
- Biometrics, Token Based (JWT)

## 2. CORS, CSRF, SQLi, XSS:-

- CORS(Cross Origin Resource Sharing) is a security mechanism used for allowing which domains are allowed to access resources. Access-Control-Allow-Origin header is used.

- CSRF(Cross-Site Request Forgery) is an web security attack that induce an user to perform such tasks which they are not intended to do. These attacks are done with the intention to perform malicious activity by the user. Ex: If a user is logged in the bank account and its session is active, the attacker might send a url to the user like of transfering the amount from user's account to attacker's account. If the attacker somehow manages to let user click on the link, so the request is sent to bank for fund transfer, so the bank will perform the operation as the user's session is active and th erequest is initiated by the user itself.

- SQL Injection- It is a code injection technique where attackers insert malicious SQL code into the input fields to manipulate the database.
- Any website using an SQL database is vulnerable to SQLi.
- To prevent it, use parameterized queries or prevent all user response.

- XSS (Cross Site Scripting) - It is a type of attack where a malicious javascript is injected into a trusted website, and that script is executed in victim's browser.
- Types:-
1. Stored XSS: Malicious scripts are stored in the database. like in user's profile bio, chat msg
2. Reflected XSS: Script comes from url/ query parameter and is reflected back.
3. DOM-based XSS: Attack happens completely from frontend js, no server involved.
-> To prevent XSS attacks... prevent using special characters, use security HTTP headers(CSP-Content Security Policy), use 'textContent' instead of 'innerHTML'

## 3. Centralized Error Handling:-

- It is good practice where all exceptions, errors across applications are handled, resolved on one single location instead of handling them in every seperated individual routes.

## 4. Logging Levels and Structured Logs:-

- Log - It is a message about what a program is doing while running.

- 1. TRACE - Most finely-grained verbose information.
- 2. DEBUG - Enough info but less than TRACE
- 3. INFO - Expected behaviour, like Server started on port:3000
- 4. WARN - Something unexpected happened in the app, might be disturbing but that doesn't mean application failure. (Like invalid inputs)
- 5. ERROR - Something failed but app still works. (Database failure, API didn't work)
- 6. FATAL - System can't continue. (Like app crashes)

### Structured Logs
- The logs are written in machine readable formats like in json format instead of plaintext, several fields are attached like timestamps, metadata, userID

## 5. Unit and Integration Testing:- 

- Unit Testing - Each module of the software is tested individually. Involves white box testing(User have the access of source code and have a knowledge of business logics written)
- Tools used: Pytest(for python test cases), Mocha(js)

- Integration Testing - Each module are combined together and tested. It testes interaction between different modules/systems. 
- Tools used: Postman

## 6. Dev vs Stage vs Production Environments:-

- Development Environment is a system environment where developers write, test and analyze their code. All the experiments are done there, and alteration doesn't affect others. It usually 

- Staging Environment is like the final stage of our developed code before going to production. All the hard core testings and database migrations will be done here and so the configurations changes. Demo bhi isi environment me hota hai

- Production Environment is the live environment which is accessible to users. The final product is represented here, and the application should have much better scalability and security.

## 7. Docker Basics

- Docker is open source platform that uses containerization. It is a process of isolating units in a structured way that consists applications and their dependencies, called a container. It is mainly used to solve the problem of running an application on my machine. It ensures that application runs consistently on dev's local machine as well as on cloud servers.

- 1. DockerFile - It contains the textual information to create images. Like which OS, which runtime, which files?
- 2. Docker Image - It is the blueprint that contains everything needed to run the app, like OS, runtime, libraries, app code. Multiple containers can be made using a single image.
- 3. Containers - They are the running instances of an image.

- Containers shares the OS of the host while Virtual Machines have their seperate OS.




