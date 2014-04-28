function arrow() {
    YUI().use('arrow-wire', function(Y) {

        var mygraphic = new Y.Graphic({
            render: "#layer"
        });

        var wire = mygraphic.addShape({
            type: Y.ArrowWire,
            stroke: {
                weight: 4,
                color: "rgb(173,216,230)"
            },
            src: {
                getXY: function() {
                    return [30, 60];
                }
            },
            tgt: {
                getXY: function() {
                    return [250, 150];
                }
            }
        });

    });
}

function arrow2() {
    YUI().use('arrow-wire', function(Y) {

        var mygraphic = new Y.Graphic({
            render: "#layer2"
        });

        var wire = mygraphic.addShape({
            type: Y.ArrowWire,
            stroke: {
                weight: 4,
                color: "rgb(173,216,230)"
            },
            src: {
                getXY: function() {
                    return [300, 600];
                }
            },
            tgt: {
                getXY: function() {
                    return [250, 150];
                }
            }
        });

    });
}