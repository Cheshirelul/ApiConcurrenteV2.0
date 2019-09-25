from sanic import Sanic
from sanic.response import json
import asyncio
import motor.motor_asyncio
from datetime import datetime
import conexion
app = Sanic()
#------------------------------------------------ C O N E X I O  N M O N G O
client = motor.motor_asyncio.AsyncIOMotorClient()
client = motor.motor_asyncio.AsyncIOMotorClient('127.0.0.1', 27017, io_loop=asyncio.get_event_loop())
db = client['sensores']
collection = db['JsonData']

#------------------------------------------------

@app.route("/")
async def test(request):
	return json({"hello": "world"})
	
@app.route("/api")
async def test1(request):
	return json({"hola": "Desde la api"})
	
@app.route("/crearDB")
async def test2(request):
	DB = motor.motor_asyncio.AsyncIOMotorClient(
		'127.0.0.1', 
		27017,
		io_loop=asyncio.get_event_loop()
	)['sensores']
	Doc = DB['JsonData']
	result = await Doc.insert_one({"Hola":"Mundo"})
	#result = await Doc.find_one()
	#result = await Doc.find().tolist(None)
	return json({"R": 200})
	
@app.route("/api/post",methods=['POST'])
async def test3(request):
	print(request.json)
	return json(request.json)

@app.route("/api/postjson",methods=['POST'])
async def saveJson(request):
	content = request.json
	content.update({"FECHA":datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
	#print(content)
	#result = await db.JsonData.insert_one(content)
	#print(result)
	DB = motor.motor_asyncio.AsyncIOMotorClient(
		'127.0.0.1', 
		27017,
		io_loop=asyncio.get_event_loop()
	)['sensores']
	Doc = DB['JsonData']
	result = await Doc.insert_one(content)
	print(content)
	print(result.inserted_id)
	return json({"R": 200})

@app.route("/api/postjsonPrueba",methods=['POST'])
async def saveJsonN(request):
	content = request.json
	content.update({"fecha":datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
	#conexion.insertarDatos(content)
	result = await collection.insert_one(content)
	print(content)
	print(result.inserted_id)
	return json({"R":200})

#--------------------------------------- este es para pruebas
@app.route('/api/mostrar', methods = ['GET'])
async def prueba2(request):
		DB = motor.motor_asyncio.AsyncIOMotorClient(
		'127.0.0.1', 
		27017,
		io_loop=asyncio.get_event_loop()
		)['sensores']
		Doc = DB['JsonData']
		#datosNodemcu2 = [doc for doc in Doc.find({},{"_id":0})]
		#cursor = db.test_collection.find({},{"_id":0})

		datosNodemcu2 = [doc for doc in await Doc.find({},{"_id":0}).to_list(length=100)]
		#print(datosNodemcu2)
		return json(datosNodemcu2)

@app.route('/api/mostrarPrueba', methods = ['GET'])
async def prueba22(request):

		datosNodemcu2 = [doc for doc in await collection.find({},{"_id":0}).to_list(length=100)]
		#print(datosNodemcu2)
		return json(datosNodemcu2)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)
