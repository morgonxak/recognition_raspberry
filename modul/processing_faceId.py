'''
Модуль для проверки распознования миц и для дообучения CVM, Knn нейронных сетей
'''
import face_recognition
import pickle
import os
from modul.trening_models_cvm_knn import branch_4


class processing_faceid:

    def __init__(self, path_classificator):
        '''

        :param queue: Задания
        :param model_cvm: открытые модели
        :param model_knn: открытые модели
        :param face_detector: Открытая модель лица
        :param path_madel:
        :param door:
        '''

        self.path_classification = path_classificator
        self.model_cvm = None
        self.model_knn = None
        self.mode_update_classificator = False
        self.load_classificator()


    def update_classificator(self, pathDatabese):
        '''
        Обновить классификатор
        :return:
        '''
        branch_4(os.path.join(pathDatabese, 'dataBase_1.pk'), pathDatabese)
        os.remove(os.path.join(pathDatabese, 'dataBase_1.pk'))
        self.mode_update_classificator = True


    def load_classificator(self):
        '''
        загрузка классификатора
        :return:
        '''
        print("загрузка классификатора")
        print(os.path.join(self.path_classification, 'knn_model_1.pk'))
        self.model_knn = pickle.load(open(os.path.join(self.path_classification, 'knn_model_1.pk'), 'rb'))
        self.model_cvm = pickle.load(open(os.path.join(self.path_classification, 'svm_model_1.pk'), 'rb'))

        return 0

    def get_descriptor_RGB(self, fase_RGB_200_200):
        '''
        создаем дискриптор для RGBизображения
        :param fase_RGB_200_200:
        :return:
        '''
        face_encoding = face_recognition.face_encodings(fase_RGB_200_200)
        return face_encoding

    def __predict_cvm(self, face_encoding):
        '''
        Проверяет пользователя по модели CVM
        :param face_encoding: Получаем дескриптор
        :return: person_id -- Уникальный идентификатор пользователя
        '''
        # Прогнозирование всех граней на тестовом изображении с использованием обученного классификатора
        try:
            person_id = self.model_cvm.predict(face_encoding)
        except ValueError:
            person_id = None

        return person_id

    def __predict_knn(self, face_encoding, tolerance=0.4):
        '''
        Проверяет пользователя по модели knn
        :param face_encoding:
        :param tolerance: Коэфициент похожести
        :return: person_id, dist == уникальный идентификатор и дистанция до него
        '''
        try:
            closest_distances = self.model_knn.kneighbors(face_encoding, n_neighbors=1)

            are_matches = [closest_distances[0][i][0] <= tolerance for i in range(1)]

            if are_matches[0]:
                person_id = self.model_knn.predict(face_encoding)[0]
            else:
                person_id = "Unknown"
        except ValueError:
            person_id = None

        return person_id

    def predict_freme(self, fase_RGB):


        if self.mode_update_classificator:
            self.mode_update_classificator = False

            self.load_classificator()

        print(fase_RGB.shape)
        descriptor_fase_RGB = self.get_descriptor_RGB(fase_RGB)

        res_predict_cvm = self.__predict_cvm(descriptor_fase_RGB)
        res_predict_knn = self.__predict_knn(descriptor_fase_RGB)

        if res_predict_cvm == res_predict_knn:
            if not res_predict_cvm is None:
                return res_predict_cvm[0]

        return None







