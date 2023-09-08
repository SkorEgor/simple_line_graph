from gui import Ui_Dialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib

matplotlib.use("Qt5Agg")


# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        # ПОЛЯ КЛАССА
        # Параметры 1 графика
        self.ax1 = None
        self.fig1 = None
        self.canvas1 = None
        self.toolbar1 = None

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        # Создаем окно
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс

        # Initialize the figure in our window
        self.initialize_figure()  # Initialize!

        # Отрисовка графика
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.plotting_without_noise(a, b)

    def initialize_figure(self, draw=False):
        # Инициализирует фигуру matplotlib внутри контейнера GUI.
        # Вызываем только один раз при инициализации

        # Создание фигуры (self.fig и self.ax)
        self.fig1 = Figure()  # Prep empty figure
        self.ax1 = self.fig1.add_subplot(111)  # Prep empty plot
        # Создание холста
        self.canvas1 = FigureCanvas(self.fig1)
        self.plotLayout.addWidget(self.canvas1)
        if draw:
            self.canvas1.draw()

        # Создание Toolbar
        self.toolbar1 = NavigationToolbar(self.canvas1, self.plotWindow,
                                          coordinates=True)
        self.plotLayout.addWidget(self.toolbar1)

    def plotting_without_noise(self, data_x, data_y):
        # Очищаем график
        self.ax1.clear()
        # Задаем название осей
        self.ax1.set_xlabel('frequency')
        self.ax1.set_ylabel('gamma')

        # Строим график
        self.ax1.plot(data_x, data_y, color='r', label='empty')

        # Убеждаемся, что все помещается внутри холста
        self.fig1.tight_layout()
        # Показываем новую фигуру в интерфейсе
        self.canvas1.draw()
