<h1>GeoDjango with Django REST API</h1>

<h2>Use Case</h2>
Many transportation suppliers that are wanted to be integrated cannot give  concrete zip codes, cities, etc that they serve.

To combat this, in this solution - it was defined custom polygons as their "service area" so that the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for company employees to do this boring grunt work.

<u>Requirement:</u>
<ul>
<li>Build a JSON REST API with CRUD operations for Provider (name, email, phone number, language and currency) and ServiceArea (name, price, geojson information)</li>

<li>Create a specific endpoint that takes a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price should be returned for each polygon. </li>
<li>Use unit tests to test your API</li>
</ul>
<h3> Description of using API: </h3>
<ul>
<li>To see all Api Overview please visit: <a href="http://geodjangoapi.herokuapp.com">http://geodjangoapi.herokuapp.com </a></li>
<li>To see the list of all Providers use API: /api/providers/: <a href="http://geodjangoapi.herokuapp.com/api/providers/">http://geodjangoapi.herokuapp.com/api/providers/</a></li>
<li>To see provider detail view use API: /api/provider/[id] Example: <a href="http://geodjangoapi.herokuapp.com/api/provider/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b">http://geodjangoapi.herokuapp.com/api/provider/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b</a></li>
<li>To Create a provider use API: /api/provider-create/ Example: <a href="http://geodjangoapi.herokuapp.com/api/provider-create/">http://geodjangoapi.herokuapp.com/api/provider-create/</a></li>

</ul>


