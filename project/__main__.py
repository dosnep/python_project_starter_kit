from project.restServer.router import Router

router = Router("main")
router.app.run("0.0.0.0")
