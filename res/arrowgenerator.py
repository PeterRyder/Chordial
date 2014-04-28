q = ['a12','a13','a14','a15','a16','a1g','a21','a23','a25','a31','a32','a34','a35','a36','a41','a42','a43','a45','a46','a47','a4g','a51','a53','a56','a61','a62','a64','a65','a67','a6g','a73','a75','ag1','ag5']

for layer in q:
    print  '''YUI().use('arrow-wire', function(Y) {

        var mygraphic = new Y.Graphic({
            render: "'''+ layer +'''"
        });
        var wire = mygraphic.addShape({
            type: Y.ArrowWire,
            stroke: {
                weight: 4,
                color: "rgb(256,256,256)"
            },
            src: {
                getXY: function() {
                    return [95, 465];
                }
            },
            tgt: {
                getXY: function() {
                    return [390, 120];
                }
            }
        });
    });'''