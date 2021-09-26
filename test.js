var data ={
    "id": "locality.10571796950561660",
    "type": "Feature",
    "place_type": [
      "locality"
    ],
    "relevance": 0.95,
    "properties": {},
    "text_en-US": "Anarkli",
    "place_name_en-US": "Anarkli, Lahore, Punjab, Pakistan",
    "text": "Anarkli",
    "place_name": "Anarkli, Lahore, Punjab, Pakistan",
    "center": [
      74.3074318952858,
      31.5679445398475
    ],
    "geometry": {
      "type": "Point",
      "coordinates": [
        74.3074318952858,
        31.5679445398475
      ]
    },
    "context": [
      {
        "id": "place.5452523133782226",
        "wikidata": "Q11739",
        "text_en-US": "Lahore",
        "language_en-US": "en",
        "text": "Lahore",
        "language": "en"
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
var city = data.context[data.context.length-3].text
var region = data.context[data.context.length-2].text
var country = data.context[data.context.length-1].text

console.log(place_name);
console.log(city);
console.log(region);
console.log(country);