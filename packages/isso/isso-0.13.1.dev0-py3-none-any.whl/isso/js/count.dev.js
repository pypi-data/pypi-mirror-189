/******/ (function() { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./isso/js/app/api.js":
/*!****************************!*\
  !*** ./isso/js/app/api.js ***!
  \****************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

var Q = __webpack_require__(/*! app/lib/promise */ "./isso/js/app/lib/promise.js");
var globals = __webpack_require__(/*! app/globals */ "./isso/js/app/globals.js");

"use strict";

var salt = "Eech7co8Ohloopo9Ol6baimi",
    location = function() { return window.location.pathname };

var script, endpoint,
    js = document.getElementsByTagName("script");

// prefer `data-isso="//host/api/endpoint"` if provided
for (var i = 0; i < js.length; i++) {
    if (js[i].hasAttribute("data-isso")) {
        endpoint = js[i].getAttribute("data-isso");
        break;
    }
}

// if no async-script is embedded, use the last script tag of `js`
if (! endpoint) {
    for (i = 0; i < js.length; i++) {
        if (js[i].getAttribute("async") || js[i].getAttribute("defer")) {
            throw "Isso's automatic configuration detection failed, please " +
                  "refer to https://github.com/posativ/isso#client-configuration " +
                  "and add a custom `data-isso` attribute.";
        }
    }

    script = js[js.length - 1];
    endpoint = script.src.substring(0, script.src.length - "/js/embed.min.js".length);
}

//  strip trailing slash
if (endpoint[endpoint.length - 1] === "/") {
    endpoint = endpoint.substring(0, endpoint.length - 1);
}

var curl = function(method, url, data, resolve, reject) {

    var xhr = new XMLHttpRequest();

    function onload() {

        var date = xhr.getResponseHeader("Date");
        if (date !== null) {
            globals.offset.update(new Date(date));
        }

        var cookie = xhr.getResponseHeader("X-Set-Cookie");
        if (cookie && cookie.match(/^isso-/)) {
            document.cookie = cookie;
        }

        if (xhr.status >= 500) {
            if (reject) {
                reject(xhr.body);
            }
        } else {
            resolve({status: xhr.status, body: xhr.responseText});
        }
    }

    try {
        xhr.open(method, url, true);
        xhr.withCredentials = true;
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                onload();
            }
        };
    } catch (exception) {
        (reject || console.log)(exception.message);
    }

    xhr.send(data);
};

var qs = function(params) {
    var rv = "";
    for (var key in params) {
        if (params.hasOwnProperty(key) &&
            params[key] !== null && typeof(params[key]) !== "undefined") {
            rv += key + "=" + encodeURIComponent(params[key]) + "&";
        }
    }

    return rv.substring(0, rv.length - 1);  // chop off trailing "&"
};

var create = function(tid, data) {
    var deferred = Q.defer();
    curl("POST", endpoint + "/new?" + qs({uri: tid || location()}), JSON.stringify(data),
        function (rv) {
            if (rv.status === 201 || rv.status === 202) {
                deferred.resolve(JSON.parse(rv.body));
            } else {
                deferred.reject(rv.body);
            }
        });
    return deferred.promise;
};

var modify = function(id, data) {
    var deferred = Q.defer();
    curl("PUT", endpoint + "/id/" + id, JSON.stringify(data), function (rv) {
        if (rv.status === 403) {
            deferred.reject("Not authorized to modify this comment!");
        } else if (rv.status === 200) {
            deferred.resolve(JSON.parse(rv.body));
        } else {
            deferred.reject(rv.body);
        }
    });
    return deferred.promise;
};

var remove = function(id) {
    var deferred = Q.defer();
    curl("DELETE", endpoint + "/id/" + id, null, function(rv) {
        if (rv.status === 403) {
            deferred.reject("Not authorized to remove this comment!");
        } else if (rv.status === 200) {
            deferred.resolve(JSON.parse(rv.body) === null);
        } else {
            deferred.reject(rv.body);
        }
    });
    return deferred.promise;
};

var view = function(id, plain) {
    var deferred = Q.defer();
    curl("GET", endpoint + "/id/" + id + "?" + qs({plain: plain}), null,
        function(rv) { deferred.resolve(JSON.parse(rv.body)); });
    return deferred.promise;
};

var fetch = function(tid, limit, nested_limit, parent, lastcreated) {
    if (typeof(limit) === 'undefined') { limit = "inf"; }
    if (typeof(nested_limit) === 'undefined') { nested_limit = "inf"; }
    if (typeof(parent) === 'undefined') { parent = null; }

    var query_dict = {uri: tid || location(), after: lastcreated, parent: parent};

    if(limit !== "inf") {
        query_dict['limit'] = limit;
    }
    if(nested_limit !== "inf"){
        query_dict['nested_limit'] = nested_limit;
    }

    var deferred = Q.defer();
    curl("GET", endpoint + "/?" +
        qs(query_dict), null, function(rv) {
            if (rv.status === 200) {
                deferred.resolve(JSON.parse(rv.body));
            } else {
                deferred.reject(rv.body);
            }
        });
    return deferred.promise;
};

var config = function() {
    var deferred = Q.defer();
    curl("GET", endpoint + "/config", null, function(rv) {
        if (rv.status === 200) {
            deferred.resolve(JSON.parse(rv.body));
        } else {
            deferred.reject(rv.body);
        }
    });
    return deferred.promise;
};

var count = function(urls) {
    var deferred = Q.defer();
    curl("POST", endpoint + "/count", JSON.stringify(urls), function(rv) {
        if (rv.status === 200) {
            deferred.resolve(JSON.parse(rv.body));
        } else {
            deferred.reject(rv.body);
        }
    });
    return deferred.promise;
};

var like = function(id) {
    var deferred = Q.defer();
    curl("POST", endpoint + "/id/" + id + "/like", null,
        function(rv) { deferred.resolve(JSON.parse(rv.body)); });
    return deferred.promise;
};

var dislike = function(id) {
    var deferred = Q.defer();
    curl("POST", endpoint + "/id/" + id + "/dislike", null,
        function(rv) { deferred.resolve(JSON.parse(rv.body)); });
    return deferred.promise;
};


var feed = function(tid) {
    return endpoint + "/feed?" + qs({uri: tid || location()});
};

var preview = function(text) {
    var deferred = Q.defer();
    curl("POST", endpoint + "/preview", JSON.stringify({text: text}),
         function(rv) {
             if (rv.status === 200) {
                 deferred.resolve(JSON.parse(rv.body).text);
             } else {
                 deferred.reject(rv.body);
             }
         });
    return deferred.promise;
};

module.exports = {
    endpoint: endpoint,
    salt: salt,
    create: create,
    modify: modify,
    remove: remove,
    view: view,
    fetch: fetch,
    count: count,
    like: like,
    dislike: dislike,
    feed: feed,
    preview: preview,
    config: config,
};


/***/ }),

/***/ "./isso/js/app/config.js":
/*!*******************************!*\
  !*** ./isso/js/app/config.js ***!
  \*******************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

var default_config = __webpack_require__(/*! app/default_config */ "./isso/js/app/default_config.js");
var utils = __webpack_require__(/*! app/utils */ "./isso/js/app/utils.js");

"use strict";

// Preserve default values to filter out when comparing
// with values fetched from server
var config = {};
for (var key in default_config) {
    config[key] = default_config[key];
}

var js = document.getElementsByTagName("script");

for (var i = 0; i < js.length; i++) {
    for (var j = 0; j < js[i].attributes.length; j++) {
        var attr = js[i].attributes[j];
        if (/^data-isso-/.test(attr.name)) {
            try {
                config[attr.name.substring(10)] = JSON.parse(attr.value);
            } catch (ex) {
                config[attr.name.substring(10)] = attr.value;
            }
        }
    }
}

// split avatar-fg on whitespace
config["avatar-fg"] = config["avatar-fg"].split(" ");

// create an array of normalized language codes from:
//   - config["lang"], if it is nonempty
//   - the first of navigator.languages, navigator.language, and
//     navigator.userLanguage that exists and has a nonempty value
//   - config["default-lang"]
//   - "en" as an ultimate fallback
// i18n.js will use the first code in this array for which we have
// a translation.
var languages = [];
var found_navlang = false;
if (config["lang"]) {
    languages.push(utils.normalize_bcp47(config["lang"]));
}
if (navigator.languages) {
    for (i = 0; i < navigator.languages.length; i++) {
        if (navigator.languages[i]) {
            found_navlang = true;
            languages.push(utils.normalize_bcp47(navigator.languages[i]));
        }
    }
}
if (!found_navlang && navigator.language) {
    found_navlang = true;
    languages.push(utils.normalize_bcp47(navigator.language));
}
if (!found_navlang && navigator.userLanguage) {
    found_navlang = true;
    languages.push(utils.normalize_bcp47(navigator.userLanguage));
}
if (config["default-lang"]) {
    languages.push(utils.normalize_bcp47(config["default-lang"]));
}
languages.push("en");

config["langs"] = languages;
// code outside this file should look only at langs
delete config["lang"];
delete config["default-lang"];

// Convert page-author-hash into a array by splitting at whitespace and/or commas
config["page-author-hashes"] = config["page-author-hashes"].split(/[\s,]+/);

module.exports = config;


/***/ }),

/***/ "./isso/js/app/count.js":
/*!******************************!*\
  !*** ./isso/js/app/count.js ***!
  \******************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

var api = __webpack_require__(/*! app/api */ "./isso/js/app/api.js");
var $ = __webpack_require__(/*! app/dom */ "./isso/js/app/dom.js");
var i18n = __webpack_require__(/*! app/i18n */ "./isso/js/app/i18n.js");

module.exports = function () {

    var objs = {};

    $.each("a", function(el) {
        if (! el.href.match || ! el.href.match(/#isso-thread$/)) {
            return;
        }

        var tid = el.getAttribute("data-isso-id") ||
                  el.href.match(/^(.+)#isso-thread$/)[1]
                         .replace(/^.*\/\/[^\/]+/, '');

        if (tid in objs) {
            objs[tid].push(el);
        } else {
            objs[tid] = [el];
        }
    });

    var urls = Object.keys(objs);

    if (urls.length > 0) {
        api.count(urls).then(function(rv) {
            for (var key in objs) {
                if (objs.hasOwnProperty(key)) {

                    var index = urls.indexOf(key);

                    for (var i = 0; i < objs[key].length; i++) {
                        objs[key][i].textContent = i18n.pluralize("num-comments", rv[index]);
                    }
                }
            }
        });
    }
};


/***/ }),

/***/ "./isso/js/app/default_config.js":
/*!***************************************!*\
  !*** ./isso/js/app/default_config.js ***!
  \***************************************/
/***/ (function(module) {

"use strict";


var default_config = {
    "css": true,
    "css-url": null,
    "lang": null,
    "default-lang": "en",
    "reply-to-self": false,
    "require-email": false,
    "require-author": false,
    "reply-notifications": false,
    "reply-notifications-default-enabled": false,
    "max-comments-top": "inf",
    "max-comments-nested": 5,
    "reveal-on-click": 5,
    "gravatar": false,
    "avatar": true,
    "avatar-bg": "#f0f0f0",
    "avatar-fg": ["#9abf88", "#5698c4", "#e279a3", "#9163b6",
                  "#be5168", "#f19670", "#e4bf80", "#447c69"].join(" "),
    "vote": true,
    "vote-levels": null,
    "feed": false,
    "page-author-hashes": "",
};
Object.freeze(default_config);

module.exports = default_config;


/***/ }),

/***/ "./isso/js/app/dom.js":
/*!****************************!*\
  !*** ./isso/js/app/dom.js ***!
  \****************************/
/***/ (function(module) {

"use strict";


function Element(node) {
    this.obj = node;

    this.replace = function (el) {
        var element = DOM.htmlify(el);
        node.parentNode.replaceChild(element.obj, node);
        return element;
    };

    this.prepend = function (el) {
        var element = DOM.htmlify(el);
        node.insertBefore(element.obj, node.firstChild);
        return element;
    };

    this.append = function (el) {
        var element = DOM.htmlify(el);
        node.appendChild(element.obj);
        return element;
    };

    this.insertAfter = function(el) {
        var element = DOM.htmlify(el);
        node.parentNode.insertBefore(element.obj, node.nextSibling);
        return element;
    };

    /**
     * Shortcut for `Element.addEventListener`, prevents default event
     * by default, set :param prevents: to `false` to change that behavior.
     */
    this.on = function(type, listener, prevent) {
        node.addEventListener(type, function(event) {
            listener(event);
            if (prevent === undefined || prevent) {
                event.preventDefault();
            }
        });
    };

    /**
     * Toggle between two internal states on event :param type: e.g. to
     * cycle form visibility. Callback :param a: is called on first event,
     * :param b: next time.
     *
     * You can skip to the next state without executing the callback with
     * `toggler.next()`. You can prevent a cycle when you call `toggler.wait()`
     * during an event.
     */
    this.toggle = function(type, a, b) {

        var toggler = new Toggle(a, b);
        this.on(type, function() {
            toggler.next();
        });
    };

    this.detach = function() {
        // Detach an element from the DOM and return it.
        node.parentNode.removeChild(this.obj);
        return this;
    };

    this.remove = function() {
        // IE quirks
        node.parentNode.removeChild(this.obj);
    };

    this.show = function() {
        node.style.display = "block";
    };

    this.hide = function() {
        node.style.display = "none";
    };

    this.setText = function(text) {
        node.textContent = text;
    };

    this.setHtml = function(html) {
        node.innerHTML = html;
    };

    this.blur = function() { node.blur() };
    this.focus = function() { node.focus() };
    this.scrollIntoView = function(args) { node.scrollIntoView(args) };

    this.checked = function() { return node.checked; };

    this.setAttribute = function(key, value) { node.setAttribute(key, value) };
    this.getAttribute = function(key) { return node.getAttribute(key) };

    this.classList = node.classList;

    Object.defineProperties(this, {
        "textContent": {
            get: function() { return node.textContent; },
            set: function(textContent) { node.textContent = textContent; }
        },
        "innerHTML": {
            get: function() { return node.innerHTML; },
            set: function(innerHTML) { node.innerHTML = innerHTML; }
        },
        "value": {
            get: function() { return node.value; },
            set: function(value) { node.value = value; }
        },
        "placeholder": {
            get: function() { return node.placeholder; },
            set: function(placeholder) { node.placeholder = placeholder; }
        }
    });
}

var Toggle = function(a, b) {
    this.state = false;

    this.next = function() {
        if (! this.state) {
            this.state = true;
            a(this);
        } else {
            this.state = false;
            b(this);
        }
    };

    this.wait = function() {
        this.state = ! this.state;
    };
};

var DOM = function(query, root, single) {
    /*
    jQuery-like CSS selector which returns on :param query: either a
    single node (unless single=false), a node list or null.

    :param root: only queries within the given element.
     */

    if (typeof single === "undefined") {
        single = true;
    }

    if (! root) {
        root = window.document;
    }

    if (root instanceof Element) {
        root = root.obj;
    }
    var elements = [].slice.call(root.querySelectorAll(query), 0);

    if (elements.length === 0) {
        return null;
    }

    if (elements.length === 1 && single) {
        return new Element(elements[0]);
    }

    // convert NodeList to Array
    elements = [].slice.call(elements, 0);

    return elements.map(function(el) {
        return new Element(el);
    });
};

DOM.htmlify = function(el) {
    /*
    Convert :param html: into an Element (if not already).
    */

    if (el instanceof Element) {
        return el;
    }

    if (el instanceof window.Element) {
        return new Element(el);
    }

    var wrapper = DOM.new("div");
    wrapper.innerHTML = el;
    return new Element(wrapper.firstChild);
};

DOM.new = function(tag, content) {
    /*
    A helper to build HTML with pure JS. You can pass class names and
    default content as well:

        var par = DOM.new("p"),
            div = DOM.new("p.some.classes"),
            div = DOM.new("textarea.foo", "...")
     */

    var el = document.createElement(tag.split(".")[0]);
    tag.split(".").slice(1).forEach(function(val) { el.classList.add(val); });

    if (["A", "LINK"].indexOf(el.nodeName) > -1) {
        el.href = "#";
    }

    if (!content && content !== 0) {
        content = "";
    }
    if (["TEXTAREA", "INPUT"].indexOf(el.nodeName) > -1) {
        el.value = content;
    } else {
        el.textContent = content;
    }
    return el;
};

DOM.each = function(tag, func) {
    // XXX really needed? Maybe better as NodeList method
    Array.prototype.forEach.call(document.getElementsByTagName(tag), func);
};

module.exports = DOM;


/***/ }),

/***/ "./isso/js/app/globals.js":
/*!********************************!*\
  !*** ./isso/js/app/globals.js ***!
  \********************************/
/***/ (function(module) {

"use strict";


var Offset = function() {
    this.values = [];
};

Offset.prototype.update = function(remoteTime) {
    this.values.push((new Date()).getTime() - remoteTime.getTime());
};

Offset.prototype.localTime = function() {
    return new Date((new Date()).getTime() - this.values.reduce(
        function(a, b) { return a + b; }) / this.values.length);
};

var offset = new Offset();

module.exports = {
    offset: offset,
}


/***/ }),

/***/ "./isso/js/app/i18n.js":
/*!*****************************!*\
  !*** ./isso/js/app/i18n.js ***!
  \*****************************/
/***/ (function(module, __unused_webpack_exports, __webpack_require__) {

"use strict";


var config = __webpack_require__(/*! app/config */ "./isso/js/app/config.js");

var catalogue = {
    bg:      __webpack_require__(/*! app/i18n/bg */ "./isso/js/app/i18n/bg.js"),
    cs:      __webpack_require__(/*! app/i18n/cs */ "./isso/js/app/i18n/cs.js"),
    da:      __webpack_require__(/*! app/i18n/da */ "./isso/js/app/i18n/da.js"),
    de:      __webpack_require__(/*! app/i18n/de */ "./isso/js/app/i18n/de.js"),
    en:      __webpack_require__(/*! app/i18n/en */ "./isso/js/app/i18n/en.js"),
    el:      __webpack_require__(/*! app/i18n/el_GR */ "./isso/js/app/i18n/el_GR.js"),
    eo:      __webpack_require__(/*! app/i18n/eo */ "./isso/js/app/i18n/eo.js"),
    es:      __webpack_require__(/*! app/i18n/es */ "./isso/js/app/i18n/es.js"),
    fa:      __webpack_require__(/*! app/i18n/fa */ "./isso/js/app/i18n/fa.js"),
    fi:      __webpack_require__(/*! app/i18n/fi */ "./isso/js/app/i18n/fi.js"),
    fr:      __webpack_require__(/*! app/i18n/fr */ "./isso/js/app/i18n/fr.js"),
    hr:      __webpack_require__(/*! app/i18n/hr */ "./isso/js/app/i18n/hr.js"),
    hu:      __webpack_require__(/*! app/i18n/hu */ "./isso/js/app/i18n/hu.js"),
    it:      __webpack_require__(/*! app/i18n/it */ "./isso/js/app/i18n/it.js"),
    ko:      __webpack_require__(/*! app/i18n/ko */ "./isso/js/app/i18n/ko.js"),
    nl:      __webpack_require__(/*! app/i18n/nl */ "./isso/js/app/i18n/nl.js"),
    oc:      __webpack_require__(/*! app/i18n/oc */ "./isso/js/app/i18n/oc.js"),
    pl:      __webpack_require__(/*! app/i18n/pl */ "./isso/js/app/i18n/pl.js"),
    pt:      __webpack_require__(/*! app/i18n/pt_BR */ "./isso/js/app/i18n/pt_BR.js"),
    "pt-BR": __webpack_require__(/*! app/i18n/pt_BR */ "./isso/js/app/i18n/pt_BR.js"),
    "pt-PT": __webpack_require__(/*! app/i18n/pt_PT */ "./isso/js/app/i18n/pt_PT.js"),
    ru:      __webpack_require__(/*! app/i18n/ru */ "./isso/js/app/i18n/ru.js"),
    sk:      __webpack_require__(/*! app/i18n/sk */ "./isso/js/app/i18n/sk.js"),
    sv:      __webpack_require__(/*! app/i18n/sv */ "./isso/js/app/i18n/sv.js"),
    tr:      __webpack_require__(/*! app/i18n/tr */ "./isso/js/app/i18n/tr.js"),
    uk:      __webpack_require__(/*! app/i18n/uk */ "./isso/js/app/i18n/uk.js"),
    vi:      __webpack_require__(/*! app/i18n/vi */ "./isso/js/app/i18n/vi.js"),
    zh:      __webpack_require__(/*! app/i18n/zh_CN */ "./isso/js/app/i18n/zh_CN.js"),
    "zh-CN": __webpack_require__(/*! app/i18n/zh_CN */ "./isso/js/app/i18n/zh_CN.js"),
    "zh-TW": __webpack_require__(/*! app/i18n/zh_TW */ "./isso/js/app/i18n/zh_TW.js"),
};

var pluralforms = function(lang) {
    // we currently only need to look at the primary language
    // subtag.
    switch (lang.split("-", 1)[0]) {
    case "bg":
    case "cs":
    case "da":
    case "de":
    case "el":
    case "en":
    case "eo":
    case "es":
    case "fa":
    case "fi":
    case "hr":
    case "hu":
    case "it":
    case "ko":
    case "nl":
    case "pt":
    case "sv":
    case "tr":
    case "vi":
    case "zh":
        return function(msgs, n) {
            return msgs[n === 1 ? 0 : 1];
        };
    case "fr":
    case "oc":
        return function(msgs, n) {
            return msgs[n > 1 ? 1 : 0];
        };
    case "ru":
    case "uk":
        return function(msgs, n) {
            if (n % 10 === 1 && n % 100 !== 11) {
                return msgs[0];
            } else if (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20)) {
                return msgs[1];
            } else {
                return typeof msgs[2] !== "undefined" ? msgs[2] : msgs[1];
            }
        };
    case "pl":
        return function(msgs, n) {
            if (n === 1) {
                return msgs[0];
            } else if (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20)) {
                return msgs[1];
            } else {
                return typeof msgs[2] !== "undefined" ? msgs[2] : msgs[1];
            }
        };
    case "sk":
        return function(msgs, n) {
            if (n === 1) {
                return msgs[0];
            } else if (n === 2 || n === 3 || n === 4) {
                return msgs[1];
            } else {
                return typeof msgs[2] !== "undefined" ? msgs[2] : msgs[1];
            }
        };
    default:
        return null;
    }
};

// for each entry in config.langs, see whether we have a catalogue
// entry and a pluralforms entry for it.  if we don't, try chopping
// off everything but the primary language subtag, before moving
// on to the next one.
var lang, plural, translations;
for (var i = 0; i < config.langs.length; i++) {
    lang = config.langs[i];
    plural = pluralforms(lang);
    translations = catalogue[lang];
    if (plural && translations)
        break;
    if (/-/.test(lang)) {
        lang = lang.split("-", 1)[0];
        plural = pluralforms(lang);
        translations = catalogue[lang];
        if (plural && translations)
            break;
    }
}

// absolute backstop; if we get here there's a bug in config.js
if (!plural || !translations) {
    lang = "en";
    plural = pluralforms(lang);
    translations = catalogue[lang];
}

var translate = function(msgid) {
    return config[msgid + '-text-' + lang] ||
      translations[msgid] ||
      catalogue.en[msgid] ||
      "[?" + msgid + "]";
};

var pluralize = function(msgid, n) {
    var msg;

    msg = translate(msgid);
    if (msg.indexOf("\n") > -1) {
        msg = plural(msg.split("\n"), (+ n));
    }

    return msg ? msg.replace("{{ n }}", (+ n)) : msg;
};

var ago = function(localTime, date) {

    var secs = ((localTime.getTime() - date.getTime()) / 1000);

    if (isNaN(secs) || secs < 0 ) {
        secs = 0;
    }

    var mins = Math.floor(secs / 60), hours = Math.floor(mins / 60),
        days = Math.floor(hours / 24);

    return secs  <=  45 && translate("date-now")  ||
           secs  <=  90 && pluralize("date-minute", 1) ||
           mins  <=  45 && pluralize("date-minute", mins) ||
           mins  <=  90 && pluralize("date-hour", 1) ||
           hours <=  22 && pluralize("date-hour", hours) ||
           hours <=  36 && pluralize("date-day", 1) ||
           days  <=   5 && pluralize("date-day", days) ||
           days  <=   8 && pluralize("date-week", 1) ||
           days  <=  21 && pluralize("date-week", Math.floor(days / 7)) ||
           days  <=  45 && pluralize("date-month", 1) ||
           days  <= 345 && pluralize("date-month", Math.floor(days / 30)) ||
           days  <= 547 && pluralize("date-year", 1) ||
                           pluralize("date-year", Math.floor(days / 365.25));
};

module.exports = {
    ago: ago,
    lang: lang,
    translate: translate,
    pluralize: pluralize,
};


/***/ }),

/***/ "./isso/js/app/i18n/bg.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/bg.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Въведете коментара си тук (поне 3 знака)",
    "postbox-author": "Име/псевдоним (незадължително)",
    "postbox-email": "Ел. поща (незадължително)",
    "postbox-website": "Уебсайт (незадължително)",
    "postbox-preview": "преглед",
    "postbox-edit": "Редактиране",
    "postbox-submit": "Публикуване",
    "num-comments": "1 коментар\n{{ n }} коментара",
    "no-comments": "Все още няма коментари",
    "comment-reply": "Отговор",
    "comment-edit": "Редактиране",
    "comment-save": "Запис",
    "comment-delete": "Изтриване",
    "comment-confirm": "Потвърждение",
    "comment-close": "Затваряне",
    "comment-cancel": "Отказ",
    "comment-deleted": "Коментарът е изтрит.",
    "comment-queued": "Коментарът чака на опашката за модериране.",
    "comment-anonymous": "анонимен",
    "comment-hidden": "{{ n }} скрити",
    "date-now": "сега",
    "date-minute": "преди 1 минута\nпреди {{ n }} минути",
    "date-hour": "преди 1 час\nпреди {{ n }} часа",
    "date-day": "вчера\nпреди {{ n }} дни",
    "date-week": "миналата седмица\nпреди {{ n }} седмици",
    "date-month": "миналия месец\nпреди {{ n }} месеца",
    "date-year": "миналата година\nпреди {{ n }} години"
};


/***/ }),

/***/ "./isso/js/app/i18n/cs.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/cs.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Sem napiště svůj komentář (nejméně 3 znaky)",
    "postbox-author": "Jméno (nepovinné)",
    "postbox-email": "E-mail (nepovinný)",
    "postbox-website": "Web (nepovinný)",
    "postbox-preview": "Náhled",
    "postbox-edit": "Upravit",
    "postbox-submit": "Publikovat",
    "num-comments": "Jeden komentář\n{{ n }} Komentářů",
    "no-comments": "Zatím bez komentářů",
    "comment-reply": "Odpovědět",
    "comment-edit": "Upravit",
    "comment-save": "Uložit",
    "comment-delete": "Smazat",
    "comment-confirm": "Potvrdit",
    "comment-close": "Zavřít",
    "comment-cancel": "Zrušit",
    "comment-deleted": "Komentář smazán",
    "comment-queued": "Komentář ve frontě na schválení",
    "comment-anonymous": "Anonym",
    "comment-hidden": "{{ n }} skryto",
    "date-now": "právě teď",
    "date-minute": "před minutou\npřed {{ n }} minutami",
    "date-hour": "před hodinou\npřed {{ n }} hodinami",
    "date-day": "včera\npřed {{ n }} dny",
    "date-week": "minulý týden\npřed {{ n }} týdny",
    "date-month": "minulý měsíc\npřed {{ n }} měsíci",
    "date-year": "minulý rok\npřed {{ n }} lety"
};


/***/ }),

/***/ "./isso/js/app/i18n/da.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/da.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Skriv din kommentar her (mindst 3 tegn)",
    "postbox-author": "Navn (valgfrit)",
    "postbox-email": "E-mail (valgfrit)",
    "postbox-website": "Hjemmeside (valgfrit)",
    "postbox-preview": "Forhåndsvisning",
    "postbox-edit": "Rediger",
    "postbox-submit": "Send",

    "num-comments": "En Kommentar\n{{ n }} Kommentarer",
    "no-comments": "Ingen kommentarer endnu",

    "comment-reply": "Svar",
    "comment-edit": "Rediger",
    "comment-save": "Gem",
    "comment-delete": "Fjern",
    "comment-confirm": "Bekræft",
    "comment-close": "Luk",
    "comment-cancel": "Annuller",
    "comment-deleted": "Kommentar slettet.",
    "comment-queued": "Kommentar i kø for moderation.",
    "comment-anonymous": "Anonym",
    "comment-hidden": "{{ n }} Skjult",

    "date-now": "lige nu",
    "date-minute": "et minut siden\n{{ n }} minutter siden",
    "date-hour": "en time siden\n{{ n }} timer siden",
    "date-day": "Igår\n{{ n }} dage siden",
    "date-week": "sidste uge\n{{ n }} uger siden",
    "date-month": "sidste måned\n{{ n }} måneder siden",
    "date-year": "sidste år\n{{ n }} år siden"
};


/***/ }),

/***/ "./isso/js/app/i18n/de.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/de.js ***!
  \********************************/
/***/ (function(module) {

module.exports = {
    "postbox-text": "Kommentar hier eingeben (mindestens 3 Zeichen)",
    "postbox-author": "Name (optional)",
    "postbox-author-placeholder": "Max Mustermann",
    "postbox-email": "E-Mail (optional)",
    "postbox-email-placeholder": "mustermann@beispiel.de",
    "postbox-website": "Website (optional)",
    "postbox-website-placeholder": "https://beispiel.de",
    "postbox-preview": "Vorschau",
    "postbox-edit": "Bearbeiten",
    "postbox-submit": "Abschicken",
    "postbox-notification": "wenn auf meinen Kommentar geantwortet wird, möchte ich eine E-Mail bekommen",

    "num-comments": "1 Kommentar\n{{ n }} Kommentare",
    "no-comments": "Bisher keine Kommentare",
    "atom-feed": "Atom-feed",

    "comment-reply": "Antworten",
    "comment-edit": "Bearbeiten",
    "comment-save": "Speichern",
    "comment-delete": "Löschen",
    "comment-confirm": "Bestätigen",
    "comment-close": "Schließen",
    "comment-cancel": "Abbrechen",
    "comment-deleted": "Kommentar gelöscht.",
    "comment-queued": "Kommentar muss noch freigeschaltet werden.",
    "comment-anonymous": "Anonym",
    "comment-hidden": "{{ n }} versteckt",
    "comment-page-author-suffix": "Autor",

    "date-now": "eben gerade",
    "date-minute": "vor einer Minute\nvor {{ n }} Minuten",
    "date-hour": "vor einer Stunde\nvor {{ n }} Stunden",
    "date-day": "Gestern\nvor {{ n }} Tagen",
    "date-week": "letzte Woche\nvor {{ n }} Wochen",
    "date-month": "letzten Monat\nvor {{ n }} Monaten",
    "date-year": "letztes Jahr\nvor {{ n }} Jahren"
};


/***/ }),

/***/ "./isso/js/app/i18n/el_GR.js":
/*!***********************************!*\
  !*** ./isso/js/app/i18n/el_GR.js ***!
  \***********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Γράψτε το σχόλιο εδώ (τουλάχιστον 3 χαρακτήρες)",
    "postbox-author": "Όνομα (προαιρετικό)",
    "postbox-email": "E-mail (προαιρετικό)",
    "postbox-website": "Ιστοσελίδα (προαιρετικό)",
    "postbox-preview": "Πρεμιέρα",
    "postbox-edit": "Επεξεργασία",
    "postbox-submit": "Υποβολή",
    "num-comments": "Ένα σχόλιο\n{{ n }} σχόλια",
    "no-comments": "Δεν υπάρχουν σχόλια",
    "comment-reply": "Απάντηση",
    "comment-edit": "Επεξεργασία",
    "comment-save": "Αποθήκευση",
    "comment-delete": "Διαγραφή",
    "comment-confirm": "Επιβεβαίωση",
    "comment-close": "Κλείσιμο",
    "comment-cancel": "Ακύρωση",
    "comment-deleted": "Διαγραμμένο σχόλιο ",
    "comment-queued": "Το σχόλιο αναμένει έγκριση",
    "comment-anonymous": "Ανώνυμος",
    "comment-hidden": "{{ n }} Κρυμμένα",
    "date-now": "τώρα",
    "date-minute": "πριν ένα λεπτό\nπριν {{ n }} λεπτά",
    "date-hour": "πριν μία ώρα\nπριν {{ n }} ώρες",
    "date-day": "Χτες\nπριν {{ n }} μέρες",
    "date-week": "την προηγούμενη εβδομάδα\nπριν {{ n }} εβδομάδες",
    "date-month": "τον προηγούμενο μήνα\nπριν {{ n }} μήνες",
    "date-year": "πέρυσι\nπριν {{ n }} χρόνια"
};


/***/ }),

/***/ "./isso/js/app/i18n/en.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/en.js ***!
  \********************************/
/***/ (function(module) {

module.exports = {
    "postbox-text": "Type Comment Here (at least 3 chars)",
    "postbox-author": "Name (optional)",
    "postbox-author-placeholder": "John Doe",
    "postbox-email": "E-mail (optional)",
    "postbox-email-placeholder": "johndoe@example.com",
    "postbox-website": "Website (optional)",
    "postbox-website-placeholder": "https://example.com",
    "postbox-preview": "Preview",
    "postbox-edit": "Edit",
    "postbox-submit": "Submit",
    "postbox-notification": "Subscribe to email notification of replies",

    "num-comments": "One Comment\n{{ n }} Comments",
    "no-comments": "No Comments Yet",
    "atom-feed": "Atom feed",

    "comment-reply": "Reply",
    "comment-edit": "Edit",
    "comment-save": "Save",
    "comment-delete": "Delete",
    "comment-confirm": "Confirm",
    "comment-close": "Close",
    "comment-cancel": "Cancel",
    "comment-deleted": "Comment deleted.",
    "comment-queued": "Comment in queue for moderation.",
    "comment-anonymous": "Anonymous",
    "comment-hidden": "{{ n }} Hidden",
    "comment-page-author-suffix": "Author",

    "date-now": "right now",
    "date-minute": "a minute ago\n{{ n }} minutes ago",
    "date-hour": "an hour ago\n{{ n }} hours ago",
    "date-day": "Yesterday\n{{ n }} days ago",
    "date-week": "last week\n{{ n }} weeks ago",
    "date-month": "last month\n{{ n }} months ago",
    "date-year": "last year\n{{ n }} years ago"
};


/***/ }),

/***/ "./isso/js/app/i18n/eo.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/eo.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Tajpu komenton ĉi-tie (almenaŭ 3 signoj)",
    "postbox-author": "Nomo (malnepra)",
    "postbox-email": "Retadreso (malnepra)",
    "postbox-website": "Retejo (malnepra)",
    "postbox-preview": "Antaŭrigardo",
    "postbox-edit": "Redaktu",
    "postbox-submit": "Sendu",
    "num-comments": "{{ n }} komento\n{{ n }} komentoj",
    "no-comments": "Neniu komento ankoraŭ",
    "comment-reply": "Respondu",
    "comment-edit": "Redaktu",
    "comment-save": "Savu",
    "comment-delete": "Forviŝu",
    "comment-confirm": "Konfirmu",
    "comment-close": "Fermu",
    "comment-cancel": "Malfaru",
    "comment-deleted": "Komento forviŝita",
    "comment-queued": "Komento en atendovico por kontrolo.",
    "comment-anonymous": "Sennoma",
    "comment-hidden": "{{ n }} kaŝitaj",
    "date-now": "ĵus nun",
    "date-minute": "antaŭ unu minuto\nantaŭ {{ n }} minutoj",
    "date-hour": "antaŭ unu horo\nantaŭ {{ n }} horoj",
    "date-day": "hieraŭ\nantaŭ {{ n }} tagoj",
    "date-week": "lasta semajno\nantaŭ {{ n }} semajnoj",
    "date-month": "lasta monato\nantaŭ {{ n }} monatoj",
    "date-year": "lasta jaro\nantaŭ {{ n }} jaroj"
};


/***/ }),

/***/ "./isso/js/app/i18n/es.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/es.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Escriba su comentario aquí (al menos 3 caracteres)",
    "postbox-author": "Nombre (opcional)",
    "postbox-email": "E-mail (opcional)",
    "postbox-website": "Sitio web (opcional)",
    "postbox-preview": "Vista preliminar",
    "postbox-edit": "Editar",
    "postbox-submit": "Enviar",
    "num-comments": "Un Comentario\n{{ n }} Comentarios",
    "no-comments": "Sin Comentarios Todavía",
    "comment-reply": "Responder",
    "comment-edit": "Editar",
    "comment-save": "Guardar",
    "comment-delete": "Eliminar",
    "comment-confirm": "Confirmar",
    "comment-close": "Cerrar",
    "comment-cancel": "Cancelar",
    "comment-deleted": "Comentario eliminado.",
    "comment-queued": "Comentario en espera para moderación.",
    "comment-anonymous": "Anónimo",
    "comment-hidden": "{{ n }} Oculto(s)",
    "date-now": "ahora",
    "date-minute": "hace un minuto\nhace {{ n }} minutos",
    "date-hour": "hace una hora\nhace {{ n }} horas",
    "date-day": "ayer\nHace {{ n }} días",
    "date-week": "la semana pasada\nhace {{ n }} semanas",
    "date-month": "el mes pasado\nhace {{ n }} meses",
    "date-year": "el año pasado\nhace {{ n }} años"
};


/***/ }),

/***/ "./isso/js/app/i18n/fa.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/fa.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "نظر خود را اینجا بنویسید (حداقل سه نویسه)",
    "postbox-author": "اسم (اختیاری)",
    "postbox-email": "ایمیل (اختیاری)",
    "postbox-website": "سایت (اختیاری)",
    "postbox-preview": "پیش‌نمایش",
    "postbox-edit": "ویرایش",
    "postbox-submit": "ارسال",

    "num-comments": "یک نظر\n{{ n }} نظر",
    "no-comments": "هنوز نظری نوشته نشده است",

    "comment-reply": "پاسخ",
    "comment-edit": "ویرایش",
    "comment-save": "ذخیره",
    "comment-delete": "حذف",
    "comment-confirm": "تایید",
    "comment-close": "بستن",
    "comment-cancel": "انصراف",
    "comment-deleted": "نظر حذف شد.",
    "comment-queued": "نظر در صف بررسی مدیر قرار دارد.",
    "comment-anonymous": "ناشناس",
    "comment-hidden": "{{ n }} مخفی",

    "date-now": "هم اکنون",
    "date-minute": "یک دقیقه پیش\n{{ n }} دقیقه پیش",
    "date-hour": "یک ساعت پیش\n{{ n }} ساعت پیش",
    "date-day": "دیروز\n{{ n }} روز پیش",
    "date-week": "یک هفته پیش\n{{ n }} هفته پیش",
    "date-month": "یک ماه پیش\n{{ n }} ماه پیش",
    "date-year": "یک سال پیش\n{{ n }} سال پیش"
};


/***/ }),

/***/ "./isso/js/app/i18n/fi.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/fi.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Kirjoita kommentti tähän (vähintään 3 merkkiä)",
    "postbox-author": "Nimi (valinnainen)",
    "postbox-email": "Sähköposti (valinnainen)",
    "postbox-website": "Web-sivu (valinnainen)",
    "postbox-preview": "Esikatselu",
    "postbox-edit": "Muokkaa",
    "postbox-submit": "Lähetä",

    "num-comments": "Yksi kommentti\n{{ n }} kommenttia",
    "no-comments": "Ei vielä kommentteja",

    "comment-reply": "Vastaa",
    "comment-edit": "Muokkaa",
    "comment-save": "Tallenna",
    "comment-delete": "Poista",
    "comment-confirm": "Vahvista",
    "comment-close": "Sulje",
    "comment-cancel": "Peru",
    "comment-deleted": "Kommentti on poistettu.",
    "comment-queued": "Kommentti on laitettu jonoon odottamaan moderointia.",
    "comment-anonymous": "Nimetön",
    "comment-hidden": "{{ n }} piilotettua",

    "date-now": "hetki sitten",
    "date-minute": "minuutti sitten\n{{ n }} minuuttia sitten",
    "date-hour": "tunti sitten\n{{ n }} tuntia sitten",
    "date-day": "eilen\n{{ n }} päivää sitten",
    "date-week": "viime viikolla\n{{ n }} viikkoa sitten",
    "date-month": "viime kuussa\n{{ n }} kuukautta sitten",
    "date-year": "viime vuonna\n{{ n }} vuotta sitten"
};


/***/ }),

/***/ "./isso/js/app/i18n/fr.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/fr.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Insérez votre commentaire ici (au moins 3 lettres)",
    "postbox-author": "Nom (optionnel)",
    "postbox-email": "Courriel (optionnel)",
    "postbox-website": "Site web (optionnel)",
    "postbox-preview": "Aperçu",
    "postbox-edit": "Éditer",
    "postbox-submit": "Soumettre",
    "postbox-notification": "S’abonner aux notifications de réponses",
    "num-comments": "{{ n }} commentaire\n{{ n }} commentaires",
    "no-comments": "Aucun commentaire pour l’instant",
    "atom-feed": "Flux Atom",
    "comment-reply": "Répondre",
    "comment-edit": "Éditer",
    "comment-save": "Enregistrer",
    "comment-delete": "Supprimer",
    "comment-confirm": "Confirmer",
    "comment-close": "Fermer",
    "comment-cancel": "Annuler",
    "comment-deleted": "Commentaire supprimé.",
    "comment-queued": "Commentaire en attente de modération.",
    "comment-anonymous": "Anonyme",
    "comment-hidden": "1 caché\n{{ n }} cachés",
    "date-now": "À l’instant",
    "date-minute": "Il y a une minute\nIl y a {{ n }} minutes",
    "date-hour": "Il y a une heure\nIl y a {{ n }} heures ",
    "date-day": "Hier\nIl y a {{ n }} jours",
    "date-week": "Il y a une semaine\nIl y a {{ n }} semaines",
    "date-month": "Il y a un mois\nIl y a {{ n }} mois",
    "date-year": "Il y a un an\nIl y a {{ n }} ans"
};


/***/ }),

/***/ "./isso/js/app/i18n/hr.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/hr.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Napiši komentar ovdje (najmanje 3 znaka)",
    "postbox-author": "Ime (neobavezno)",
    "postbox-email": "E-mail (neobavezno)",
    "postbox-website": "Web stranica (neobavezno)",
    "postbox-preview": "Pregled",
    "postbox-edit": "Uredi",
    "postbox-submit": "Pošalji",
    "num-comments": "Jedan komentar\n{{ n }} komentara",
    "no-comments": "Još nema komentara",
    "comment-reply": "Odgovori",
    "comment-edit": "Uredi",
    "comment-save": "Spremi",
    "comment-delete": "Obriši",
    "comment-confirm": "Potvrdi",
    "comment-close": "Zatvori",
    "comment-cancel": "Odustani",
    "comment-deleted": "Komentar obrisan",
    "comment-queued": "Komentar u redu za provjeru.",
    "comment-anonymous": "Anonimno",
    "comment-hidden": "{{ n }} Skrivenih",
    "date-now": "upravo",
    "date-minute": "prije minutu\nprije {{ n }} minuta",
    "date-hour": "prije sat vremena\nprije {{ n }} sati",
    "date-day": "jučer\nprije {{ n }} dana",
    "date-week": "prošli tjedan\nprije {{ n }} tjedana",
    "date-month": "prošli mjesec\nprije {{ n }} mjeseci",
    "date-year": "prošle godine\nprije {{ n }} godina"
};


/***/ }),

/***/ "./isso/js/app/i18n/hu.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/hu.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Hozzászólást ide írd be (legalább 3 betűt)",
    "postbox-author": "Név (nem kötelező)",
    "postbox-email": "Email (nem kötelező)",
    "postbox-website": "Website (nem kötelező)",
    "postbox-preview": "Előnézet",
    "postbox-edit": "Szerekesztés",
    "postbox-submit": "Elküld",
    "num-comments": "Egy hozzászólás\n{{ n }} hozzászólás",
    "no-comments": "Eddig nincs hozzászólás",
    "comment-reply": "Válasz",
    "comment-edit": "Szerekesztés",
    "comment-save": "Mentés",
    "comment-delete": "Törlés",
    "comment-confirm": "Megerősít",
    "comment-close": "Bezár",
    "comment-cancel": "Törlés",
    "comment-deleted": "Hozzászólás törölve.",
    "comment-queued": "A hozzászólást előbb ellenőrizzük.",
    "comment-anonymous": "Névtelen",
    "comment-hidden": "{{ n }} rejtve",
    "date-now": "pillanatokkal ezelőtt",
    "date-minute": "egy perce\n{{ n }} perce",
    "date-hour": "egy órája\n{{ n }} órája",
    "date-day": "tegnap\n{{ n }} napja",
    "date-week": "múlt héten\n{{ n }} hete",
    "date-month": "múlt hónapban\n{{ n }} hónapja",
    "date-year": "tavaly\n{{ n }} éve"
};


/***/ }),

/***/ "./isso/js/app/i18n/it.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/it.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Scrivi un commento qui (minimo 3 caratteri)",
    "postbox-author": "Nome (opzionale)",
    "postbox-email": "E-mail (opzionale)",
    "postbox-website": "Sito web (opzionale)",
    "postbox-preview": "Anteprima",
    "postbox-edit": "Modifica",
    "postbox-submit": "Invia",
    "num-comments": "Un Commento\n{{ n }} Commenti",
    "no-comments": "Ancora Nessun Commento",
    "comment-reply": "Rispondi",
    "comment-edit": "Modifica",
    "comment-save": "Salva",
    "comment-delete": "Elimina",
    "comment-confirm": "Conferma",
    "comment-close": "Chiudi",
    "comment-cancel": "Cancella",
    "comment-deleted": "Commento eliminato.",
    "comment-queued": "Commento in coda per moderazione.",
    "comment-anonymous": "Anonimo",
    "comment-hidden": "{{ n }} Nascosto",
    "date-now": "poco fa",
    "date-minute": "un minuto fa\n{{ n }} minuti fa",
    "date-hour": "un ora fa\n{{ n }} ore fa",
    "date-day": "Ieri\n{{ n }} giorni fa",
    "date-week": "questa settimana\n{{ n }} settimane fa",
    "date-month": "questo mese\n{{ n }} mesi fa",
    "date-year": "quest'anno\n{{ n }} anni fa"
};


/***/ }),

/***/ "./isso/js/app/i18n/ko.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/ko.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "여기에 댓글을 입력해주세요(최소 3문자 이상)",
    "postbox-author": "이름 (선택)",
    "postbox-email": "이메일 (선택)",
    "postbox-website": "웹사이트 (선택)",
    "postbox-preview": "미리보기",
    "postbox-edit": "수정",
    "postbox-submit": "댓글쓰기",
    "postbox-notification": "댓글이 달리면 이메일로 알립니다",

    "num-comments": "한 개의 댓글\n{{ n }} 개의 댓글",
    "no-comments": "아직 댓글이 없습니다",
    "atom-feed": "Atom 피드",

    "comment-reply": "댓글",
    "comment-edit": "수정",
    "comment-save": "저장",
    "comment-delete": "삭제",
    "comment-confirm": "확인",
    "comment-close": "닫기",
    "comment-cancel": "취소",
    "comment-deleted": "댓글이 삭제됨.",
    "comment-queued": "검토 대기 중인 댓글.",
    "comment-anonymous": "익명",
    "comment-hidden": "{{ n }} 개의 숨김 댓글",

    "date-now": "방금 전",
    "date-minute": "1 분 전\n{{ n }} 분 전",
    "date-hour": "1 시간 전\n{{ n }} 시간 전",
    "date-day": "어제\n{{ n }} 일 전",
    "date-week": "저번 주\n{{ n }} 주 전",
    "date-month": "저번 달\n{{ n }} 개월 전",
    "date-year": "작년\n{{ n }} 년 전"
};


/***/ }),

/***/ "./isso/js/app/i18n/nl.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/nl.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Typ reactie hier (minstens 3 karakters)",
    "postbox-author": "Naam (optioneel)",
    "postbox-email": "E-mail (optioneel)",
    "postbox-website": "Website (optioneel)",
    "postbox-preview": "Voorbeeld",
    "postbox-edit": "Bewerken",
    "postbox-submit": "Versturen",
    "num-comments": "Één reactie\n{{ n }} reacties",
    "no-comments": "Nog geen reacties",
    "comment-reply": "Beantwoorden",
    "comment-edit": "Bewerken",
    "comment-save": "Opslaan",
    "comment-delete": "Verwijderen",
    "comment-confirm": "Bevestigen",
    "comment-close": "Sluiten",
    "comment-cancel": "Annuleren",
    "comment-deleted": "Reactie verwijderd.",
    "comment-queued": "Reactie staat in de wachtrij voor goedkeuring.",
    "comment-anonymous": "Anoniem",
    "comment-hidden": "{{ n }} verborgen",
    "date-now": "zojuist",
    "date-minute": "een minuut geleden\n{{ n }} minuten geleden",
    "date-hour": "een uur geleden\n{{ n }} uur geleden",
    "date-day": "gisteren\n{{ n }} dagen geleden",
    "date-week": "vorige week\n{{ n }} weken geleden",
    "date-month": "vorige maand\n{{ n }} maanden geleden",
    "date-year": "vorig jaar\n{{ n }} jaar geleden"
};


/***/ }),

/***/ "./isso/js/app/i18n/oc.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/oc.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Escriure lo comentari aquí (almens 3 caractèrs)",
    "postbox-author": "Nom (opcional)",
    "postbox-email": "Corrièl (opcional)",
    "postbox-website": "Site web (opcional)",
    "postbox-preview": "Apercebut",
    "postbox-edit": "Modificar",
    "postbox-submit": "Enviar",
    "postbox-notification": "S'abonar per corrièl a las notificacions de responsas",

    "num-comments": "Un comentari\n{{ n }} comentaris",
    "no-comments": "Cap de comentari pel moment",
    "atom-feed": "Flux Atom",

    "comment-reply": "Respondre",
    "comment-edit": "Modificar",
    "comment-save": "Salvar",
    "comment-delete": "Suprimir",
    "comment-confirm": "Confirmar",
    "comment-close": "Tampar",
    "comment-cancel": "Anullar",
    "comment-deleted": "Comentari suprimit.",
    "comment-queued": "Comentari en espèra de moderacion.",
    "comment-anonymous": "Anonim",
    "comment-hidden": "1 rescondut\n{{ n }} resconduts",

    "date-now": "ara meteis",
    "date-minute": "fa una minuta \nfa {{ n }} minutas",
    "date-hour": "fa una ora\nfa {{ n }} oras",
    "date-day": "Ièr\nfa {{ n }} jorns",
    "date-week": "la setmana passada\nfa {{ n }} setmanas",
    "date-month": "lo mes passat\nfa {{ n }} meses",
    "date-year": "l'an passat\nfa {{ n }} ans"
};


/***/ }),

/***/ "./isso/js/app/i18n/pl.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/pl.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Tutaj wpisz komentarz (co najmniej 3 znaki)",
    "postbox-author": "Imię/nick (opcjonalnie)",
    "postbox-email": "E-mail (opcjonalnie)",
    "postbox-website": "Strona (opcjonalnie)",
    "postbox-preview": "Podgląd",
    "postbox-edit": "Edytuj",
    "postbox-submit": "Wyślij",
    "postbox-notification": "Otrzymuj powiadomienia o odpowiedziach na e-mail",

    "num-comments": "Jeden komentarz\n{{ n }} komentarze\n{{ n }} komentarzy",
    "no-comments": "Nie ma jeszcze komentarzy",
    "atom-feed": "Kanał Atom",

    "comment-reply": "Odpowiedz",
    "comment-edit": "Edytuj",
    "comment-save": "Zapisz",
    "comment-delete": "Usuń",
    "comment-confirm": "Potwierdź",
    "comment-close": "Zamknij",
    "comment-cancel": "Anuluj",
    "comment-deleted": "Komentarz usunięty.",
    "comment-queued": "Komentarz w kolejce do moderacji.",
    "comment-anonymous": "Anonim",
    "comment-hidden": "{{ n }} ukryty\n{{ n }} ukryte\n{{ n }} ukrytych",

    "date-now": "teraz",
    "date-minute": "minutę temu\n{{ n }} minuty temu\n{{ n }} minut temu",
    "date-hour": "godzinę temu\n{{ n }} godziny temu\n{{ n }} godzin temu",
    "date-day": "wczoraj\n{{ n }} dni temu",
    "date-week": "w ubiegłym tygodniu\n{{ n }} tygodnie temu\n{{ n }} tygodni temu",
    "date-month": "w ubiegłym miesiącu\n{{ n }} miesiące temu\n{{ n }} miesięcy temu",
    "date-year": "w ubiegłym roku\n{{ n }} lata temu\n{{ n }} lat temu"
};


/***/ }),

/***/ "./isso/js/app/i18n/pt_BR.js":
/*!***********************************!*\
  !*** ./isso/js/app/i18n/pt_BR.js ***!
  \***********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Digite seu comentário aqui (pelo menos 3 letras)",
    "postbox-author": "Nome (opcional)",
    "postbox-email": "E-mail (opcional)",
    "postbox-website": "Website (opcional)",
    "postbox-preview": "Prévia",
    "postbox-edit": "Editar",
    "postbox-submit": "Enviar",
    "postbox-notification": "Receber emails de notificação de respostas",

    "num-comments": "Um Comentário\n{{ n }} Comentários",
    "no-comments": "Nenhum comentário ainda",
    "atom-feed": "Feed Atom",

    "comment-reply": "Responder",
    "comment-edit": "Editar",
    "comment-save": "Salvar",
    "comment-delete": "Excluir",
    "comment-confirm": "Confirmar",
    "comment-close": "Fechar",
    "comment-cancel": "Cancelar",
    "comment-deleted": "Comentário apagado.",
    "comment-queued": "Comentário na fila de moderação.",
    "comment-anonymous": "Anônimo",
    "comment-hidden": "{{ n }} Oculto(s)",

    "date-now": "agora mesmo",
    "date-minute": "um minuto atrás\n{{ n }} minutos atrás",
    "date-hour": "uma hora atrás\n{{ n }} horas atrás",
    "date-day": "ontem\n{{ n }} dias",
    "date-week": "semana passada\n{{ n }} semanas atrás",
    "date-month": "mês passado\n{{ n }} meses atrás",
    "date-year": "ano passado\n{{ n }} anos atrás"
};


/***/ }),

/***/ "./isso/js/app/i18n/pt_PT.js":
/*!***********************************!*\
  !*** ./isso/js/app/i18n/pt_PT.js ***!
  \***********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Escreva o seu comentário aqui (pelo menos 3 letras)",
    "postbox-author": "Nome (opcional)",
    "postbox-email": "E-mail (opcional)",
    "postbox-website": "Website (opcional)",
    "postbox-preview": "Testar",
    "postbox-edit": "Editar",
    "postbox-submit": "Enviar",
    "postbox-notification": "Receber emails de notificação de respostas",

    "num-comments": "Um Comentário\n{{ n }} Comentários",
    "no-comments": "Nenhum comentário ainda",
    "atom-feed": "Feed Atom",

    "comment-reply": "Responder",
    "comment-edit": "Editar",
    "comment-save": "Guardar",
    "comment-delete": "Excluir",
    "comment-confirm": "Confirmar",
    "comment-close": "Fechar",
    "comment-cancel": "Cancelar",
    "comment-deleted": "Comentário apagado.",
    "comment-queued": "Comentário na fila de moderação.",
    "comment-anonymous": "Anónimo",
    "comment-hidden": "{{ n }} Oculto(s)",

    "date-now": "agora mesmo",
    "date-minute": "um minuto atrás\n{{ n }} minutos atrás",
    "date-hour": "uma hora atrás\n{{ n }} horas atrás",
    "date-day": "ontem\n{{ n }} dias",
    "date-week": "semana passada\n{{ n }} semanas atrás",
    "date-month": "mês passado\n{{ n }} meses atrás",
    "date-year": "ano passado\n{{ n }} anos atrás"
};


/***/ }),

/***/ "./isso/js/app/i18n/ru.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/ru.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Оставить комментарий (минимум 3 символа)",
    "postbox-author": "Имя (необязательно)",
    "postbox-email": "Email (необязательно)",
    "postbox-website": "Сайт (необязательно)",
    "postbox-preview": "Предпросмотр",
    "postbox-edit": "Правка",
    "postbox-submit": "Отправить",
    "postbox-notification": "Подписаться на уведомление об ответах",
    "num-comments": "{{ n }} комментарий\n{{ n }} комментария\n{{ n }} комментариев",
    "no-comments": "Пока нет комментариев",
    "comment-reply": "Ответить",
    "comment-edit": "Правка",
    "comment-save": "Сохранить",
    "comment-delete": "Удалить",
    "comment-confirm": "Подтвердить удаление",
    "comment-close": "Закрыть",
    "comment-cancel": "Отменить",
    "comment-deleted": "Комментарий удалён",
    "comment-queued": "Комментарий будет проверен модератором",
    "comment-anonymous": "Аноним",
    "comment-hidden": "Скрыт {{ n }} комментарий\nСкрыто {{ n }} комментария\nСкрыто {{ n }} комментариев",
    "date-now": "Только что",
    "date-minute": "{{ n }} минуту назад\n{{ n }} минуты назад\n{{ n }} минут назад",
    "date-hour": "{{ n }} час назад\n{{ n }} часа назад\n{{ n }} часов назад",
    "date-day": "{{ n }} день назад\n{{ n }} дня назад\n{{ n }} дней назад",
    "date-week": "{{ n }} неделю назад\n{{ n }} недели назад\n{{ n }} недель назад",
    "date-month": "{{ n }} месяц назад\n{{ n }} месяца назад\n{{ n }} месяцев назад",
    "date-year": "{{ n }} год назад\n{{ n }} года назад\n{{ n }} лет назад"
};


/***/ }),

/***/ "./isso/js/app/i18n/sk.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/sk.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Sem napíšte svoj komentár (minimálne 3 znaky)",
    "postbox-author": "Meno (nepovinné)",
    "postbox-email": "E-mail (nepovinný)",
    "postbox-website": "Web (nepovinný)",
    "postbox-preview": "Náhľad",
    "postbox-edit": "Upraviť",
    "postbox-submit": "Publikovať",
    "num-comments": "Jeden komentár\n{{ n }} komentáre\n{{ n }} komentárov",
    "no-comments": "Zatiaľ bez komentárov",
    "comment-reply": "Odpovedať",
    "comment-edit": "Upraviť",
    "comment-save": "Uložiť",
    "comment-delete": "Zmazať",
    "comment-confirm": "Potvrdit",
    "comment-close": "Zavrieť",
    "comment-cancel": "Zrušiť",
    "comment-deleted": "Komentár bol vymazaný",
    "comment-queued": "Komentár zaradený na schválenie",
    "comment-anonymous": "Anonym",
    "comment-hidden": "{{ n }} skrytý\n{{ n }} skryté\n{{ n }} skrytých",
    "date-now": "práve teraz",
    "date-minute": "pred minútou\npred {{ n }} minútami",
    "date-hour": "pred hodinou\npred {{ n }} hodinami",
    "date-day": "včera\npred {{ n }} dňami",
    "date-week": "minulý týždeň\npred {{ n }} týždňami",
    "date-month": "minulý mesiac\npred {{ n }} mesiacmi",
    "date-year": "minulý rok\npred {{ n }} rokmi"
};


/***/ }),

/***/ "./isso/js/app/i18n/sv.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/sv.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Skriv din kommentar här (minst 3 tecken)",
    "postbox-author": "Namn (frivilligt)",
    "postbox-email": "E-mail (frivilligt)",
    "postbox-website": "Hemsida (frivilligt)",
    "postbox-preview": "Förhandsvisning",
    "postbox-edit": "Redigera",
    "postbox-submit": "Skicka",
    "num-comments": "En kommentar\n{{ n }} kommentarer",
    "no-comments": "Inga kommentarer än",
    "comment-reply": "Svara",
    "comment-edit": "Redigera",
    "comment-save": "Spara",
    "comment-delete": "Radera",
    "comment-confirm": "Bekräfta",
    "comment-close": "Stäng",
    "comment-cancel": "Avbryt",
    "comment-deleted": "Kommentar raderad.",
    "comment-queued": "Kommentaren inväntar granskning.",
    "comment-anonymous": "Anonym",
    "comment-hidden": "{{ n }} Gömd",
    "date-now": "just nu",
    "date-minute": "en minut sedan\n{{ n }} minuter sedan",
    "date-hour": "en timme sedan\n{{ n }} timmar sedan",
    "date-day": "igår\n{{ n }} dagar sedan",
    "date-week": "förra veckan\n{{ n }} veckor sedan",
    "date-month": "förra månaden\n{{ n }} månader sedan",
    "date-year": "förra året\n{{ n }} år sedan"
};


/***/ }),

/***/ "./isso/js/app/i18n/tr.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/tr.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Yorumunuzu buraya yazın (en az üç karakter)",
    "postbox-author": "İsim (zorunlu değil)",
    "postbox-email": "E-posta (zorunlu değil)",
    "postbox-website": "Web sitesi (zorunlu değil)",
    "postbox-preview": "Ön izleme",
    "postbox-edit": "Düzenle",
    "postbox-submit": "Gönder",
    "postbox-notification": "Yanıtlar için e-posta bildirimlerine abone ol",

    "num-comments": "Bir yorum\n{{ n }} yorum",
    "no-comments": "Henüz yorum yok",
    "atom-feed": "Atom akışı",

    "comment-reply": "Yanıtla",
    "comment-edit": "Düzenle",
    "comment-save": "Kaydet",
    "comment-delete": "Sil",
    "comment-confirm": "Onayla",
    "comment-close": "Kapat",
    "comment-cancel": "İptal",
    "comment-deleted": "Yorum silindi.",
    "comment-queued": "Yorumunuz yönetici onayını bekliyor.",
    "comment-anonymous": "Anonim",
    "comment-hidden": "{{ n }} gizli",

    "date-now": "şimdi",
    "date-minute": "bir dakika önce\n{{ n }} dakika önce",
    "date-hour": "bir saat önce\n{{ n }} saat önce",
    "date-day": "dün\n{{ n }} gün önce",
    "date-week": "geçen hafta\n{{ n }} hafta önce",
    "date-month": "geçen ay\n{{ n }} ay önce",
    "date-year": "geçen yıl\n{{ n }} yıl önce"
};


/***/ }),

/***/ "./isso/js/app/i18n/uk.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/uk.js ***!
  \********************************/
/***/ (function(module) {

module.exports = {
  "postbox-text": "Введіть коментар тут (принаймні 3 символи)",
  "postbox-author": "Ім'я (необов'язково)",
  "postbox-author-placeholder": "John Doe",
  "postbox-email": "Пошта (необов'язково)",
  "postbox-email-placeholder": "johndoe@example.com",
  "postbox-website": "Веб-сайт (необов'язково)",
  "postbox-website-placeholder": "https://example.com",
  "postbox-preview": "Прев'ю",
  "postbox-edit": "Редагувати",
  "postbox-submit": "Відправити",
  "postbox-notification": "Підписатися на повідомлення про відповіді поштою",

  "num-comments": "{{ n }} коментар\n{{ n }} коментарі\n{{ n }} коментарів",
  "no-comments": "Коментарів поки нема",
  "atom-feed": "Атомна стрічка",

  "comment-reply": "Відповісти",
  "comment-edit": "Редагувати",
  "comment-save": "Зберегти",
  "comment-delete": "Видалити",
  "comment-confirm": "Підтвердити",
  "comment-close": "Закрити",
  "comment-cancel": "Скасувати",
  "comment-deleted": "Коментар видалено.",
  "comment-queued": "Коментар в черзі на модерацію.",
  "comment-anonymous": "Анонімний",
  "comment-hidden": "{{ n }} Прихований",
  "comment-page-author-suffix": "Автор",

  "date-now": "прямо зараз",
  "date-minute": "хвилину тому\n{{ n }} хвилини тому\n{{ n }}хвилин тому",
  "date-hour": "годину тому\n{{ n }} години тому\n{{ n }} годин тому",
  "date-day": "Вчора\n{{ n }} дні тому\n{{ n }} днів тому",
  "date-week": "минулого тижня\n{{ n }} тижні тому\n{{ n }} тижнів тому",
  "date-month": "останній місяць\n{{ n }} місяці тому\n{{ n }} місяців тому",
  "date-year": "минулого року\n{{ n }} роки тому\n{{ n }} років тому"
};


/***/ }),

/***/ "./isso/js/app/i18n/vi.js":
/*!********************************!*\
  !*** ./isso/js/app/i18n/vi.js ***!
  \********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "Nhập bình luận tại đây (tối thiểu 3 ký tự)",
    "postbox-author": "Tên (tùy chọn)",
    "postbox-email": "E-mail (tùy chọn)",
    "postbox-website": "Website (tùy chọn)",
    "postbox-preview": "Xem trước",
    "postbox-edit": "Sửa",
    "postbox-submit": "Gửi",
    "postbox-notification": "Nhận thông báo email cho các bình luận phản hồi",

    "num-comments": "Một bình luận\n{{ n }} bình luận",
    "no-comments": "Chưa có bình luận nào",

    "comment-reply": "Trả lời",
    "comment-edit": "Sửa",
    "comment-save": "Lưu",
    "comment-delete": "Xóa",
    "comment-confirm": "Xác nhận",
    "comment-close": "Đóng",
    "comment-cancel": "Hủy",
    "comment-deleted": "Đã xóa bình luận.",
    "comment-queued": "Bình luận đang chờ duyệt",
    "comment-anonymous": "Nặc danh",
    "comment-hidden": "{{ n }} đã ẩn",

    "date-now": "vừa mới",
    "date-minute": "một phút trước\n{{ n }} phút trước",
    "date-hour": "một giờ trước\n{{ n }} giờ trước",
    "date-day": "Hôm qua\n{{ n }} ngày trước",
    "date-week": "Tuần qua\n{{ n }} tuần trước",
    "date-month": "Tháng trước\n{{ n }} tháng trước",
    "date-year": "Năm trước\n{{ n }} năm trước"
};


/***/ }),

/***/ "./isso/js/app/i18n/zh_CN.js":
/*!***********************************!*\
  !*** ./isso/js/app/i18n/zh_CN.js ***!
  \***********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "在此输入评论 (最少 3 个字符)",
    "postbox-author": "名字 (可选)",
    "postbox-email": "电子邮箱 (可选)",
    "postbox-website": "网站 (可选)",
    "postbox-preview": "预览",
    "postbox-edit": "编辑",
    "postbox-submit": "提交",
    "postbox-notification": "有新回复时发送邮件通知",

    "num-comments": "1 条评论\n{{ n }} 条评论",
    "no-comments": "还没有评论",

    "comment-reply": "回复",
    "comment-edit": "编辑",
    "comment-save": "保存",
    "comment-delete": "删除",
    "comment-confirm": "确认",
    "comment-close": "关闭",
    "comment-cancel": "取消",
    "comment-deleted": "评论已删除.",
    "comment-queued": "评论待审核.",
    "comment-anonymous": "匿名",
    "comment-hidden": "{{ n }} 条评论已隐藏",

    "date-now": "刚刚",
    "date-minute": "1 分钟前\n{{ n }} 分钟前",
    "date-hour": "1 小时前\n{{ n }} 小时前",
    "date-day": "昨天\n{{ n }} 天前",
    "date-week": "上周\n{{ n }} 周前",
    "date-month": "上个月\n{{ n }} 个月前",
    "date-year": "去年\n{{ n }} 年前"
};


/***/ }),

/***/ "./isso/js/app/i18n/zh_TW.js":
/*!***********************************!*\
  !*** ./isso/js/app/i18n/zh_TW.js ***!
  \***********************************/
/***/ (function(module) {

module.exports= {
    "postbox-text": "在此輸入留言 (至少 3 個字元)",
    "postbox-author": "名稱 (非必填)",
    "postbox-email": "電子信箱 (非必填)",
    "postbox-website": "個人網站 (非必填)",
    "postbox-preview": "預覽",
    "postbox-edit": "編輯",
    "postbox-submit": "送出",
    "postbox-notification": "訂閱回覆的電子郵件通知",

    "num-comments": "1 則留言\n{{ n }} 則留言",
    "no-comments": "尚無留言",

    "comment-reply": "回覆",
    "comment-edit": "編輯",
    "comment-save": "儲存",
    "comment-delete": "刪除",
    "comment-confirm": "確認",
    "comment-close": "關閉",
    "comment-cancel": "取消",
    "comment-deleted": "留言已刪",
    "comment-queued": "留言待審",
    "comment-anonymous": "匿名",
    "comment-hidden": "{{ n }} 則隱藏留言",

    "date-now": "剛剛",
    "date-minute": "1 分鐘前\n{{ n }} 分鐘前",
    "date-hour": "1 小時前\n{{ n }} 小時前",
    "date-day": "昨天\n{{ n }} 天前",
    "date-week": "上週\n{{ n }} 週前",
    "date-month": "上個月\n{{ n }} 個月前",
    "date-year": "去年\n{{ n }} 年前"
};


/***/ }),

/***/ "./isso/js/app/lib/promise.js":
/*!************************************!*\
  !*** ./isso/js/app/lib/promise.js ***!
  \************************************/
/***/ (function(module) {

"use strict";


var stderr = function(text) { console.log(text); };

var Promise = function() {
    this.success = [];
    this.errors = [];
};

Promise.prototype.then = function(onSuccess, onError) {
    this.success.push(onSuccess);
    if (onError) {
        this.errors.push(onError);
    } else {
        this.errors.push(stderr);
    }
};

var Defer = function() {
    this.promise = new Promise();
};

Defer.prototype = {
    promise: Promise,
    resolve: function(rv) {
        this.promise.success.forEach(function(callback) {
            window.setTimeout(function() {
                callback(rv);
            }, 0);
        });
    },

    reject: function(error) {
        this.promise.errors.forEach(function(callback) {
            window.setTimeout(function() {
                callback(error);
            }, 0);
        });
    }
};

var when = function(obj, func) {
    if (obj instanceof Promise) {
        return obj.then(func);
    } else {
        return func(obj);
    }
};

var defer = function() { return new Defer(); };

module.exports = {
    defer: defer,
    when: when,
};


/***/ }),

/***/ "./isso/js/app/lib/ready.js":
/*!**********************************!*\
  !*** ./isso/js/app/lib/ready.js ***!
  \**********************************/
/***/ (function(module) {

"use strict";


var loaded = false;
var once = function(callback) {
    if (! loaded) {
        loaded = true;
        callback();
    }
};

var domready = function(callback) {

    // HTML5 standard to listen for dom readiness
    document.addEventListener('DOMContentLoaded', function() {
        once(callback);
    });

    // if dom is already ready, just run callback
    if (document.readyState === "interactive" || document.readyState === "complete" ) {
        once(callback);
    }
};

module.exports = domready;


/***/ }),

/***/ "./isso/js/app/utils.js":
/*!******************************!*\
  !*** ./isso/js/app/utils.js ***!
  \******************************/
/***/ (function(module) {

"use strict";


// return `cookie` string if set
var cookie = function(cookie) {
    return (document.cookie.match('(^|; )' + cookie + '=([^;]*)') || 0)[2];
};

var pad = function(n, width, z) {
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
};

// Normalize a BCP47 language tag.
// Quoting https://tools.ietf.org/html/bcp47 :
//   An implementation can reproduce this format without accessing
//   the registry as follows.  All subtags, including extension
//   and private use subtags, use lowercase letters with two
//   exceptions: two-letter and four-letter subtags that neither
//   appear at the start of the tag nor occur after singletons.
//   Such two-letter subtags are all uppercase (as in the tags
//   "en-CA-x-ca" or "sgn-BE-FR") and four-letter subtags are
//   titlecase (as in the tag "az-Latn-x-latn").
// We also map underscores to dashes.
var normalize_bcp47 = function(tag) {
    var subtags = tag.toLowerCase().split(/[_-]/);
    var afterSingleton = false;
    for (var i = 0; i < subtags.length; i++) {
        if (subtags[i].length === 1) {
            afterSingleton = true;
        } else if (afterSingleton || i === 0) {
            afterSingleton = false;
        } else if (subtags[i].length === 2) {
            subtags[i] = subtags[i].toUpperCase();
        } else if (subtags[i].length === 4) {
            subtags[i] = subtags[i].charAt(0).toUpperCase()
                + subtags[i].substr(1);
        }
    }
    return subtags.join("-");
};

// Safari private browsing mode supports localStorage, but throws QUOTA_EXCEEDED_ERR
var localStorageImpl;
try {
    localStorage.setItem("x", "y");
    localStorage.removeItem("x");
    localStorageImpl = localStorage;
} catch (ex) {
    localStorageImpl = (function(storage) {
        return {
            setItem: function(key, val) {
                storage[key] = val;
            },
            getItem: function(key) {
                return typeof(storage[key]) !== 'undefined' ? storage[key] : null;
            },
            removeItem: function(key) {
                delete storage[key];
            }
        };
    })({});
}

// Check if something is ready, and if not, register self as listener to be
// triggered once it is ready
var wait_for = function() {
    var listeners = [];
    var is_ready = false;
    return {
        is_ready: function(){return is_ready},
        register: function(listener) {
            // Ignore duplicate listeners
            if (listeners.indexOf(listener) < 0) {
                listeners.push(listener);
            };
        },
        reset: function() { is_ready = false },
        on_ready: function() {
            is_ready = true;
            for (var listener in listeners) {
                // Ignore dead listeners
                if (!listeners[listener]) {
                    continue;
                }
                // Run listener
                listeners[listener]();
            }
            // Clear listeners
            listeners = [];
        },
    };
};

module.exports = {
    cookie: cookie,
    localStorageImpl: localStorageImpl,
    normalize_bcp47: normalize_bcp47,
    pad: pad,
    wait_for: wait_for,
};


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
!function() {
/*!**************************!*\
  !*** ./isso/js/count.js ***!
  \**************************/
var domready = __webpack_require__(/*! app/lib/ready */ "./isso/js/app/lib/ready.js");
var count = __webpack_require__(/*! app/count */ "./isso/js/app/count.js");

domready(function() {
    count();
});

}();
/******/ })()
;
//# sourceMappingURL=count.dev.js.map