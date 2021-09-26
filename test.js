var data = {
  "id": "poi.257698095444",
  "type": "Feature",
  "place_type": [
    "poi"
  ],
  "relevance": 0.9375,
  "properties": {
    "landmark": true,
    "address": "Railway Ticket Ghar Rd",
    "foursquare": "4fa93266e4b0542abae6b517"
  },
  "text_en-US": "Khanewal Railway Station",
  "place_name_en-US": "Khanewal Railway Station, Railway Ticket Ghar Rd, Khanewal, Punjab, Pakistan",
  "text": "Khanewal Railway Station",
  "place_name": "Khanewal Railway Station, Railway Ticket Ghar Rd, Khanewal, Punjab, Pakistan",
  "center": [
    71.930116,
    30.309601
  ],
  "geometry": {
    "coordinates": [
      71.930116,
      30.309601
    ],
    "type": "Point"
  },
  "context": [
    {
      "id": "place.19797953469279620",
      "text_en-US": "Khanewal",
      "text": "Khanewal"
    },
    {
      "id": "region.8926719562277000",
      "wikidata": "Q4478",
      "short_code": "PK-PB",
      "text_en-US": "Punjab",
      "language_en-US": "en",
      "text": "Punjab",
      "language": "en"
    },
    {
      "id": "country.2377117351",
      "wikidata": "Q843",
      "short_code": "pk",
      "text_en-US": "Pakistan",
      "language_en-US": "en",
      "text": "Pakistan",
      "language": "en"
    }
  ]
}


var longitude = data.center[0]
var latitude = data.center[1]
var place_name = data.place_name
// var country = data.context[data.context.length-1].text
// var region = data.context[data.context.length-2].text
// var city = data.context[data.context.length-3].text

var new_data  = data['place_name_en-US'].split(',')
var country = new_data[new_data.length-1]
var region = new_data[new_data.length-2]
var city = new_data[new_data.length-3]