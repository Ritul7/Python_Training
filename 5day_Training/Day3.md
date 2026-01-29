# DAY 3 Notes:-

## 1. Server

- Server is hardware or software systems or both that serves something, that provides services, data, resources to other computers (client) on a network.
- Server includes hardware and software components.
- - Hardware is nothing but high powered machine with specialized components build for continuous operations. Includes CPUs, GPUs, RAM, storage
- - Sofrware

- 1. Browser: An application that allows us to navigate through diff websites on the internet. (Ex: Chrome, FireFox, OperaMini)
- 2. Search Engine: Is a website within the browser that finds information for us. (Ex: Google, Yahoo)

- Web Browser ko install kiya jata h, Search Engine ko install nhi krte
- Web Browser doesn't have its own db, uses only temp storage for cache and cookies. Search engine ka db hota hai

### Client-Server Model:-

- 1. Client: Any app or software that requests info or services from the server. Like Web browser(Chrome) or Email apps(gmail).
- 2. Server: A powerful system that listens for and process the client's request by performing and then delievering tasks.

### 
- A server can also act as a client, like application server requests database server while responding to the client simultaneously.

### How DNS Works??

1. When we enter the domain name in a browser, our computer starts processing the corresponding IP address needed to connect to the website.
2. First our computer looks for local cache for that IP address.
3. If not found then our computer looks for host files ( manually configured domain names ot ip addresses).
4. If not found locally, then req is sent to a DNS resolver. 
    - DNS resolver is provided by the ISP(Internet Service Provider) or public DNS service like Google DNS or CLoudfare.
    - DNS resolver is like a intermediate which connects with various other servers.
5. The DNS resolver first goes to Root Server, it doesn't know the exact IP address but directs us to respective domain TLD. Ex: www.google.com . So, root server directs us to    .com TLD server.
6. So, DNS resolver queries the .com TLD server for .com domains. The TLD server knows where to find authoritative nameserver of www.google.com.
7. The DNS Resolver then query authoritative nameserver for www.google.com. This Authoritative Nameserver is responsible for storing DNS records for the domain and responds back the exact IP Address to the resolver.
8. The DNS Resolver sends the IP Address to the computer and the website loads.

## 2. Blocking and Non-Blocking Execution:-

- When the execution of program is synchronous, as it waits for the one task to complete before moving to the execution of the another task.
- Non-Blocking means, the execution flow doesn't wait for a task to complete for its execution. 

### Thread
- It is the smallest execution unit of the process. Multiple threads works together in a single process to execute multiple tasks simultaneously.
 
## 3. Event Loop:-

- It is a mechanism which is used to handle Blocking and Non-Blocking Operations of a program. It ensures that the execution of the program should be smooth and doesn't lags.

console.log("1");

setTimeout(()=>{
    console.log("execution 1");
}, 2000)

console.log("2");

setTimeout(()=>{
    console.log("execution 2");
}, 0) 

- Here the first setTimeout fn is sent to browser as it is blocking in behaviour, similarly second setTimeout fn is also sent to the browser. When they completes their execution, sent to the callback queue in serial order(jo pehle complete hua wo pehle queue me jayega) and callback queue continuously checks ki whether call stack is empty or not, if empty then they are sent to call stack and executed.

## 4. Routing and Middleware:- 

- Routing means specifying seperate paths for accessing various things.
- Static Routing - Here, Route paths are fixed.
- Dynamic Routing - Here, Route paths contains variable as the part of URL, that are often used to  access specific resources. Route parameters - /users/123 This path uses:id for accessing user woth userID :123.

1. Middleware is a function that runs between every req - res cycle.
- It contains three parts: request object, response object and the next function.
- Middlware either can end the req-res cycle by its own, or can send the execution flow to the next middleware using next() function.
- Mainly used for authentication purpose.
- Different types of middlewares are there like: App-level middleware, Router-level middleware, thirdy party middleware, built-in middlewares, custom middleware, error-handling middlware.

## 5. Authentication:- 

- It is the process of verifying user's identity to ensure they are what they claim to be.
- Authorization means determinng what the authenticated user is allow to do.

### Stateful Authentication:
- Here the state is managed by the server itself. The sessionID is created for every user and rest of the info is stored on the server. Everytime when the user comes woth their session id, the server checks for the respective session.

### Stateless Authentication:
- Here the state is managed by the client i.e. the client itself holds the info woth them in the form of token.

## 5. JWT:-

- It is a secure way of sending information btw client and server.
- Mainly used in APIs for verification purpose and to prevent unauthentified access.
- A JWT has 3 parts:         

Header.Payload.Signature

1. Header has the metadata i.e. type of algorithm used for encryption.
2. Payload contains the claims(stores the actual data).
3. Signature means taking the header, payload, algorithm (cryptographic) and the key and sign them.

### Process of Authentication using JWT:-

- First the jwt token is to be generated by the server when the user logs-in for the first time, then that token is sent back with the user. User carries the toekn with itself and server has the secret key. Whenever the user tries to login, they have to take the token with themselves and server checks it validity of the user by using the secret key it has.



