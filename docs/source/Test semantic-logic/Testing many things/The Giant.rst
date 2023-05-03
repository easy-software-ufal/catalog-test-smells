The Giant
^^^^^
Definitions:

* Many assertions in a single test case
* Many assertions in a single test case


Code Example:

.. code-block:: javascript
    
    test('should setup middleware', async () => {
        const nuxt = createNuxt()
        const server = new Server(nuxt)
        server.useMiddleware = jest.fn()
        server.serverContext = { id: 'test-server-context' }

        await server.setupMiddleware()

        expect(server.nuxt.callHook).toBeCalledTimes(2)
        expect(server.nuxt.callHook).nthCalledWith(1, 'render:setupMiddleware', server.app)
        expect(server.nuxt.callHook).nthCalledWith(2, 'render:errorMiddleware', server.app)

        expect(server.useMiddleware).toBeCalledTimes(4)
        expect(serveStatic).toBeCalledTimes(2)
        expect(serveStatic).nthCalledWith(1, 'resolve(/var/nuxt/src, var/nuxt/static)', server.options.render.static)
        expect(server.useMiddleware).nthCalledWith(1, {
            dir: 'resolve(/var/nuxt/src, var/nuxt/static)',
            id: 'test-serve-static',
            prefix: 'test-render-static-prefix'
        })
        expect(serveStatic).nthCalledWith(2, 'resolve(/var/nuxt/build, dist, client)', server.options.render.dist)
        expect(server.useMiddleware).nthCalledWith(2, {
            handler: {
            dir: 'resolve(/var/nuxt/build, dist, client)',
            id: 'test-serve-static'
            },
            path: '__nuxt_test'
        })

        const nuxtMiddlewareOpts = {
            options: server.options,
            nuxt: server.nuxt,
            renderRoute: expect.any(Function),
            resources: server.resources
        }
        expect(nuxtMiddleware).toBeCalledTimes(1)
        expect(nuxtMiddleware).toBeCalledWith(nuxtMiddlewareOpts)
        expect(server.useMiddleware).nthCalledWith(3, {
            id: 'test-nuxt-middleware',
            ...nuxtMiddlewareOpts
        })

        const errorMiddlewareOpts = {
            resources: server.resources,
            options: server.options
        }
        expect(errorMiddleware).toBeCalledTimes(1)
        expect(errorMiddleware).toBeCalledWith(errorMiddlewareOpts)
        expect(server.useMiddleware).nthCalledWith(4, {
            id: 'test-error-middleware',
            ...errorMiddlewareOpts
        })
    })

References:

 * `TDD anti patterns - Chapter 1 <https://www.codurance.com/publications/tdd-anti-patterns-chapter-1>`_
 * `TDD anti-patterns - the liar, excessive setup, the giant, slow poke <https://marabesi.com/tdd/2021/08/28/tdd-anti-patterns.html>`_

