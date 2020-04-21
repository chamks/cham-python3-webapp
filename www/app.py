from aiohttp import web
import logging; logging.basicConfig(level=logging.INFO)

routes = web.RouteTableDef()

@routes.get("/")
async def index(request):
    return web.Response(text = "hello,cham")

def init():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app,port = 8888,host = "127.0.0.1")
    logging.info("Server started at loaclhost!")

init()