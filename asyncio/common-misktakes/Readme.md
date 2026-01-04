Blocking I/O inside asynchronous code

Problem: Synchronous libraries (such as requests) are used inside coroutines, blocking the event loop and wasting the benefits of asynchronous programming.

Fix: Replace blocking libraries with asynchronous alternatives (for example, use aiohttp instead of requests) to ensure non-blocking I/O operations.

Hidden blocking operations

Problem: I/O-intensive operations may be wrapped inside asynchronous calls, making blocking behavior difficult to detect without profiling.

Fix: Use profilers such as Scalene to identify high system or I/O wait times and locate blocking code paths.

Improper session and connection handling

Problem: Creating a new HTTP connection for each request increases latency and resource usage.

Fix: Reuse a shared aiohttp.ClientSession() to take advantage of connection pooling and reduce connection overhead.

Sequential execution of coroutines

Problem: Coroutines are awaited one after another in a loop, resulting in behavior similar to synchronous code.

Fix: Launch coroutines concurrently using tools such as asyncio.create_task() or asyncio.gather().

Misinterpreting performance improvements

Problem: Reducing individual operation time is mistaken for overall scalability improvement, or vice versa.

Fix: Evaluate both total execution time (wall time) and concurrency behavior to ensure the event loop remains unblocked and fully utilized.