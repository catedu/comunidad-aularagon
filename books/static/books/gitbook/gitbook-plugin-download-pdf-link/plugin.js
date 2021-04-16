require(["gitbook", "jQuery"], function(gitbook, $) {
  gitbook.events.bind('start', function (e, config) {
    var conf = config['download-pdf-link'];
    var base = conf.base

    if (base.slice(-1) !== "/") {
      base += "/"
    }

    gitbook.toolbar.createButton({
      icon: 'fa fa-file-pdf-o',
      onClick: function() {
        window.open(base)
      }
    })
  })
})
