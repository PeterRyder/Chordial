from PyQt4.QtGui import QPainter, QStyle, QStyleOption, QWidget
 
 
class QArrow(QWidget):
    """Qt implementation similar to GtkArrow."""
 
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
  
    def __init__(self, direction, parent=None):
        """Create a new instance."""
        QWidget.__init__(self, parent)
        if not direction in (QArrow.UP, QArrow.DOWN,
                  QArrow.LEFT, QArrow.RIGHT):
            raise ValueError('Wrong arrow direction.')
        self._direction = direction
 
    def paintEvent(self, event):
        """Paint a nice primitive arrow."""
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        #painter.translate(20, 10)
        p.rotate(-45)
        if self._direction == QArrow.UP:
            primitive = QStyle.PE_IndicatorArrowUp
        elif self._direction == QArrow.DOWN:
            primitive = QStyle.PE_IndicatorArrowDown
        elif self._direction == QArrow.LEFT:
            primitive = QStyle.PE_IndicatorArrowLeft
        else:
            primitive = QStyle.PE_IndicatorArrowRight
            
        self.style().drawPrimitive(primitive, opt, p, self)