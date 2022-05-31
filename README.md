<h1>GeoDjango with Django REST API</h1>

<h2>Use Case</h2>
Many transportation suppliers that are wanted to be integrated cannot give  concrete zip codes, cities, etc that they serve.

To combat this, in this solution - it was defined custom polygons as their "service area" so that the owners of these shuttle companies to be able to define and alter their polygons whenever they want, eliminating the need for company employees to do this boring grunt work.

<u>Requirements:</u>
<ul>
<li>Build a JSON REST API with CRUD operations for Provider (name, email, phone number, language and currency) and ServiceArea (name, price, geojson information)</li>

<li>Create a specific endpoint that takes a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price should be returned for each polygon. </li>
<li>Use unit tests to test your API</li>
</ul>
<h3> Description of using API: </h3>

<h4><u>Credentials: </u></h4>
<ul>
<li>
Demo Website: <a href="http://geodjangoapi.herokuapp.com">http://geodjangoapi.herokuapp.com </a></li>
<li>
Admin Login Page: <a href="http://geodjangoapi.herokuapp.com/admin">http://geodjangoapi.herokuapp.com/admin </a></li>
<li>
-- Admin Login: admin <br>
-- Password: geodjango
</li>

</ul>

To see all Api Overview please visit: <a href="http://geodjangoapi.herokuapp.com">http://geodjangoapi.herokuapp.com </a>

<h4><u>API For Providers: </u></h4>
<ul></ul>
<li>To see the list of all Providers use API: `GET /api/providers/: <a href="http://geodjangoapi.herokuapp.com/api/providers/">http://geodjangoapi.herokuapp.com/api/providers/</a></li>
<li>To see provider detail view use API: `GET /api/provider/[id]/ Example: <a href="http://geodjangoapi.herokuapp.com/api/provider/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b">http://geodjangoapi.herokuapp.com/api/provider/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b</a></li>
<li>To Create a provider use API:`POST /api/provider-create/ Example: <a href="http://geodjangoapi.herokuapp.com/api/provider-create/">http://geodjangoapi.herokuapp.com/api/provider-create/</a></li>
<li>To Update Provider use API: `PUT /api/provider-update/[id]/ Example: <a href="http://geodjangoapi.herokuapp.com/api/provider-update/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b">http://geodjangoapi.herokuapp.com/api/provider-update/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b</a></li>
<li>To Delete Provider use API: `DELETE /api/provider-delete/[id]/ Example: <a href="http://geodjangoapi.herokuapp.com/api/provider-delete/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b">http://geodjangoapi.herokuapp.com/api/provider-delete/636fd81c-ada5-48f7-ae30-42cf8e4e7e5b</a></li>
</ul>


</ul>
<h4><u>API For Service Area: </u></h4>
<ul></ul>
<li>To see the list of all Service Areas use API: `GET /api/serviceareas/: <a href="http://geodjangoapi.herokuapp.com/api/serviceareas/">http://geodjangoapi.herokuapp.com/api/serviceareas/</a></li>
<li>To see Service Area Detail View use API: `GET /api/servicearea/[id]/ Example: <a href="http://geodjangoapi.herokuapp.com/api/servicearea/3357c9f5-891e-4996-bd49-43fb640a623a">http://geodjangoapi.herokuapp.com/api/servicearea/3357c9f5-891e-4996-bd49-43fb640a623a</a></li>
<li>To Create Service Area use API:`POST /api/servicearea-create/ Example: <a href="http://geodjangoapi.herokuapp.com/api/servicearea-create/">http://geodjangoapi.herokuapp.com/api/servicearea-create/</a></li>
<li>To Update Service Area use API: `PUT /api/servicearea-update/[id]/ Example: <a href="http://geodjangoapi.herokuapp.com/api/servicearea-update/3357c9f5-891e-4996-bd49-43fb640a623a">http://geodjangoapi.herokuapp.com/api/servicearea-update/3357c9f5-891e-4996-bd49-43fb640a623a</a></li>
<li>To Service Area use API: `DELETE /api/servicearea-delete/[id]/ Example: <a href="http://geodjangoapi.herokuapp.com/api/servicearea-delete/3357c9f5-891e-4996-bd49-43fb640a623a">http://geodjangoapi.herokuapp.com/api/servicearea-delete/3357c9f5-891e-4996-bd49-43fb640a623a</a></li>
</ul>




