import json
from urllib.parse import parse_qs
from odoo import http
from odoo.http import request

class PropertyApi(http.Controller):
    @http.route("/v1/property",methods=["POST"],type="http",auth="none",csrf=False)
    def property(self):
        # print("hello from property")
       args= request.httprequest.data.decode()
       vals = json.loads(args)
       # print(vals)

       if not vals.get('name'):
           return request.make_json_response({
               "message": "put name ya user"
           },status=400)
       try:
           res= request.env["estate.property"].create(vals)
           # print(res)
           if res:
                return request.make_json_response({
                     "message" : "hello your record created successfully",
                      "id":res.id,
                       "name":res.name
                      },status=200)
       except Exception as error:
           return request.make_json_response({
               "message": error
           })



    # json
    @http.route("/v1/property/json", methods=["POST"], type="json", auth="none", csrf=False)
    def property_json(self):
        # print("hello from property")
        args = request.httprequest.data.decode()  # get body data
        vals = json.loads(args)
        # print(vals)

        res = request.env["estate.property"].create(vals)
        # print(res)
        if res:
            return [{
                "message": "hello your record created successfully"
            }]





    @http.route("/v1/property/update/<int:estate_property_id>",methods=["PUT"],type="http",auth="none",csrf=False)
    def property_update(self,estate_property_id):
        try:
             estate_property_id = request.env["estate.property"].search([('id','=', estate_property_id)])
             if not estate_property_id:
                 return request.make_json_response({
                     "message": "id is not correct"
                 }, status=400)
             # print(estate_property_id)
             args=request.httprequest.data.decode()
             vals=json.loads(args)
             estate_property_id.write(vals)
             return request.make_json_response({
                         "message" : "hello your record updated successfully",
                          "id": estate_property_id.id,
                           "name": estate_property_id.name
                          },status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error

            },status=400)



    @http.route("/v1/property/<int:estate_property_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def property_read(self, estate_property_id):
        try:
            estate_property_id = request.env["estate.property"].search([('id', '=', estate_property_id)])
            if not estate_property_id:
                return request.make_json_response({
                    "message": "id is not correct"
                }, status=400)
            # print(estate_property_id)

            return request.make_json_response({
                "message": "hello your record data",
                "id": estate_property_id.id,
                "name": estate_property_id.name,
                "description":estate_property_id.description,
                "garden_orientation":estate_property_id.garden_orientation
            }, status=200)

        except Exception as error:
            return request.make_json_response({
                "message": error

            }, status=400)



    @http.route("/v1/property/<int:estate_property_id>", methods=["DELETE"], type="http", auth="none",
                csrf=False)
    def property_delete(self, estate_property_id):
        try:
            estate_property_id = request.env["estate.property"].search([('id', '=', estate_property_id)])
            if not estate_property_id:
                return request.make_json_response({
                    "message": "id is not correct"
                }, status=400)

            estate_property_id.unlink()
            return request.make_json_response({
                "message": "hello your record deleted successfully",

            }, status=200)
        except Exception as error:
            return request.make_json_response({
                "message": error

            }, status=400)




    @http.route("/v1/properties",methods=["GET"],type="http",auth="none",csrf=False)
    def property_record_list(self):
            try:
                 params =parse_qs(request.httprequest.query_string.decode('utf-8'))
                 estate_property_domain=[]
                 if params.get('state'):
                     estate_property_domain+=[('state','=',params.get('state')[0])]
                 estate_property_ids = request.env["estate.property"].search(estate_property_domain)
                 if not estate_property_ids:
                     return request.make_json_response({
                         "message": "No Records!"
                     }, status=400)

                 return request.make_json_response([{
                             "message" : "hello your recordlist",
                              "id": estate_property_id.id,
                             "name": estate_property_id.name,
                             "description": estate_property_id.description,
                             "garden_orientation": estate_property_id.garden_orientation
                              }for estate_property_id in estate_property_ids],status=200)
            except Exception as error:
                return request.make_json_response({
                    "message": error

                },status=400)