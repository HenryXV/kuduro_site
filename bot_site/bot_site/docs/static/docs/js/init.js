document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {edge: 'right', preventScrolling: false});
    var collapsibleElem = document.querySelector('.collapsible');
    var collapsibleInstance = M.Collapsible.init(collapsibleElem);
    var imgElems = document.querySelectorAll('.materialboxed');
    var imgInstances = M.Materialbox.init(imgElems)
});
