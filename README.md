# My Restaurant Catalog - Data Driven Web Application

## Description
Compare and contrast some of the pro's and con's of a top-down approach focusing on the front-end first versus a bottum-up approach that focus on the database and server-side code first. Using a agile code development.

## Index
1. [Bio and File info](#bio-and-file-info)
2. [Version](#version)
3. [Keywords](#keywords)
4. [Checklist](#checklist)
5. [WebBio](#webbio)
6. [WebBioImg](#webbioimg)

## Bio , File and Repo info

- ##### Author: Hugo Smits
- ##### Date of creation : 25/11/2018
- ##### Last modified : 30/11/2018
- ##### Based on Repo: [https://github.com/HugoSmits/RestaurantUdacity](https://github.com/HugoSmits/RestaurantUdacity)

## Version

##### Current version of the repository is version 2.0 .

## Keywords
- ##### Agile code development (Ready to use prototype with sucessive iterations)
- ##### DOM (Document Object Model) is an application programming interface (API) for valid HTML and well-formed XML documents.
- ##### Authorization (user authorizes a third party to access a part of his/her personal info).
- ##### Authentication (Verifies if the user is who he/she claims to be).
- ##### Authorizations happens normally after Authentication.

## Checklist

- ##### Mock ups
- ##### Routing 
- ##### Template & Forums
- ##### CRUD Functionality
- ##### API Endpoints
- ##### Styling & Message Flashing

## Features to Implement

- ##### Authentication
- ##### Social Network sign ins
- ##### Local Permission
- ##### Add API Endpoints
- ##### Securing API Endpoints
- ##### Polishing Styling

## Css Fontsize Em vs Percent
- ##### The situation is that point and pixel units are not necessarily best suited for web documents, which leaves us with the em and percent units. In theory, both the em and the percent units are identical, but in application, they actually have a few minor differences that are important to consider.
- ##### Em is the up and coming usage. Sometimes it goes against practical applications.
- ##### Percent is the trusted veteran.

## Pro's and Cons of using third party Authentication
#### Pro's:
- ##### Outsource auth handling to OAuth providers.
- ##### Easier to register users no extra form.
- ##### Less passwords for users to remember and you don't have to keep their password secure.

#### Neutral:
- ##### Users need to have a 3rd party account.

#### Cons:
- ##### Users don't trust your site.
- ##### Keep auth scopes minimal.
- ##### Limited/restricted internet access (e.g. if site is offline).
- ##### 2 factor authentication may require own Authentication.

## API Endpoints technologies
#### JSON and XML

#### JSON
- ##### Derived from JavaScript.
- ##### Can be condensed to reduce file size.
- ##### JSON is considered to most common way to structure data sent across restful API's

#### XML
- ##### Uses identifying tags similar to html.

#### SOAP vs REST architectures

#### SOAP
- ##### Must use XML for message format.
- ##### Works with HTTP and other Application layer protocols.

#### REST (Has gained alot of popularity)
- ##### Uses HTTP verbs to manage resources.
- ##### Can use any type of message format
- ##### Easier to implement

- #### REST contraints
- ##### Needs clear differention betweem client and server.
- ##### Stateless meaning it doesn't remember the clients activity during the session.
- ##### Cacheable (can be cached by the client if permitted so)
- ##### Uniform Interface
- ##### Layered System: Endpoints that rely on other endpoints.
- ##### Code on demand (Opcional)

## Hashing
- ##### Can only be used in one way
- ##### Is deterministic (Same passwords give same hashes)

## URI's
- ##### Refer to resources (in plural) and not actions of the resources.

## API's with version
- ##### Maitains usability for older users if api's are updated. (v1 , v2 , ...)

## WebAIM WCAG 2.0
- ##### Role , Label /(Name) , Value , State
	- ##### The Name of an object is, well, its name. For instance, in the case of a BUTTON element, the ‘name’ of that element would be the text within the button. For an INPUT element, the name would be its label. In other words, the name says: “What do we call this thing?”.

	- ##### The State of an object describes what this thing is currently doing, if it can do things. Implicitly, it also often describes what else this thing can do. For a checkbox, for example, its current state could be “checked”. This implies therefore that it could also be “unchecked” (unless it is readonly, of course).

	- ##### The Role of an object declares what it is. In other words, using our previous example, the object would have a role of “checkbox”. Or, more specifically, it would have whatever role that the operating system or accessibility API says is the role for checkboxes. MSAA and UIAutomation would use ‘ROLE_SYSTEM_CHECKBUTTON’ to identify its role.

	- ##### The Value of an object is, er, the value. Whether this exists or not and what its value is depends significantly on the type of object. Perhaps the easiest way to understand this would be to again use our checkbox analogy. Provided the following code: <input type="checkbox" name="agree" id="agree" value="Yes" /><label for="agree">Do you agree Karl is awesome?</label> the value for this checkbox would be ‘Yes’ (when in a checked state).

- ##### DOM order / Tab order
- ##### tabindex (Should only be for interactive content)
(FOCUS) ( -1 (of screen elements) javascript focusable , 0 (on screen elements)
and javascript focusable).
- ##### Managing Focus
- ##### ARIA
	- ##### Use High contrast when styling.
	- ##### Use additional messages to not rely on color alone.
- ##### Roving Focus
- ##### document.activeElement to search in web console(Ctrl+Shift+J) for active tab element.
- ##### Keyboard Trap (Should be avoided)
- ##### Screen Reader would get a HTML page from the 90's
- ##### DOM Tree is converted into the Acessibility Tree
- ##### Alt "label" for extra info for Screen Readers
- ##### Accessibility Developer Tools 

## WebBio
- ##### https://stackoverflow.com/questions/10503981/check-if-an-array-is-not-empty-in-jinja2
- ##### https://kyleschaeffer.com/development/css-font-size-em-vs-px-vs-pt-vs/
- ##### https://www.darkreading.com/safely-storing-user-passwords-hashing-vs-encrypting/a/d-id/1269374
- ##### https://en.wikipedia.org/wiki/Man-in-the-middle_attack
- ##### https://en.wikipedia.org/wiki/Session_hijacking
- ##### https://en.wikipedia.org/wiki/OAuth
- ##### https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb/related.

## WebBioImg
- ##### https://stocksnap.io/photo/SYDUAKYJIS
- ##### https://stocksnap.io/photo/7QH4K6AESO
- ##### https://stocksnap.io/photo/DOTNAI7BL2

