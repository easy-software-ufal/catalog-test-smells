Excessive Setup
^^^^^
**Definition:**

* Many dependencies you have to create beforehand (such as classes, operating system dependencies, databases - basically anything that removes the attention to the testing goal).

**Also Known As:**

* Large Setup Methods, Inappropriately Shared Fixture, The Mother Hen, The Stranger, The Distant Relative, The Cuckoo

**Code Example:**

.. code-block:: javascript

  jest.mock('compression')
  jest.mock('connect')
  jest.mock('serve-static')
  jest.mock('serve-placeholder')
  jest.mock('launch-editor-middleware')
  jest.mock('@nuxt/utils')
  jest.mock('@nuxt/vue-renderer')
  jest.mock('../src/listener')
  jest.mock('../src/context')
  jest.mock('../src/jsdom')
  jest.mock('../src/middleware/nuxt')
  jest.mock('../src/middleware/error')
  jest.mock('../src/middleware/timing')
  
  describe('server: server', () => {
    const createNuxt = () => ({
      options: {
        dir: {
          static: 'var/nuxt/static'
        },
        srcDir: '/var/nuxt/src',
        buildDir: '/var/nuxt/build',
        globalName: 'test-global-name',
        globals: { id: 'test-globals' },
        build: {
          publicPath: '__nuxt_test'
        },
        router: {
          base: '/foo/'
        },
        render: {
          id: 'test-render',
          dist: {
            id: 'test-render-dist'
          },
          static: {
            id: 'test-render-static',
            prefix: 'test-render-static-prefix'
          }
        },
        server: {},
        serverMiddleware: []
      },
      hook: jest.fn(),
      ready: jest.fn(),
      callHook: jest.fn(),
      resolver: {
        requireModule: jest.fn(),
        resolvePath: jest.fn().mockImplementation(p => p)
      }
    })
  
    beforeAll(() => {
      jest.spyOn(path, 'join').mockImplementation((...args) => `join(${args.join(', ')})`)
      jest.spyOn(path, 'resolve').mockImplementation((...args) => `resolve(${args.join(', ')})`)
      connect.mockReturnValue({ use: jest.fn() })
      serveStatic.mockImplementation(dir => ({ id: 'test-serve-static', dir }))
      nuxtMiddleware.mockImplementation(options => ({
        id: 'test-nuxt-middleware',
        ...options
      }))
      errorMiddleware.mockImplementation(options => ({
        id: 'test-error-middleware',
        ...options
      }))
      createTimingMiddleware.mockImplementation(options => ({
        id: 'test-timing-middleware',
        ...options
      }))
      launchMiddleware.mockImplementation(options => ({
        id: 'test-open-in-editor-middleware',
        ...options
      }))
      servePlaceholder.mockImplementation(options => ({
        key: 'test-serve-placeholder',
        ...options
      }))
    })
  }

**References:**

.. admonition:: Quality attributes

    * :octicon:`file-code;1em` -  Code Example
    * :octicon:`comment-discussion;1em` -  Cause and Effect
    * :octicon:`graph;1em` -  Frequency
    * :octicon:`sync;1em` -  Refactoring

* `Anti-Patterns - Digital Tapestry <https://digitaltapestry.net/testify/manual/AntiPatterns.html>`_
* `Categorising Test Smells <https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.696.5180&rep=rep1&type=pdf>`_ :octicon:`graph;1em`
* `TDD anti patterns - Chapter 1 <https://www.codurance.com/publications/tdd-anti-patterns-chapter-1>`_ :octicon:`file-code;1em`
* `TDD anti-patterns - the liar, excessive setup, the giant, slow poke <https://marabesi.com/tdd/2021/08/28/tdd-anti-patterns.html>`_ :octicon:`file-code;1em`
* `Test-Driven Development: TDD Anti-Patterns <https://bryanwilhite.github.io/the-funky-knowledge-base/entry/kb2076072213/>`_
* `Unit Testing Anti-Patterns, Full List <https://www.yegor256.com/2018/12/11/unit-testing-anti-patterns.html>`_
* `Unit testing Anti-patterns catalogue <https://stackoverflow.com/questions/333682/unit-testing-anti-patterns-catalogue>`_
