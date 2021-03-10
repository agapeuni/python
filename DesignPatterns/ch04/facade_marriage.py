class Hotelier(object):

    def __init__(self):
        print("결혼을 위한 호텔 마련?")

    def __isAvailable(self):
        print("호텔은 당일 행사 기간 동안 무료입니까?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("예약 등록\n\n")


class Florist(object):

    def __init__(self):
        print("행사를 위한 꽃 장식?")

    def setFlowerRequirements(self):
        print("카네이션, 장미, 백합은 장식용으로 사용됩니다.\n\n")


class Caterer(object):

    def __init__(self):
        print("행사를 위한 음식 준비")

    def setCuisine(self):
        print("중국 및 대륙별 요리 제공\n\n")


class Musician(object):

    def __init__(self):
        print("결혼을 위한 음악적인 준비들")

    def setMusicType(self):
        print("재즈와 클래식이 연주될 것이다.\n\n")


class EventManager(object):

    def __init__(self):
        print("이벤트 매니저: 사람들과 이야기해보겠습니다.\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class You(object):

    def __init__(self):
        print("You:: 우와! 결혼 준비?!!!")

    def askEventManager(self):
        print("You:: 이벤트 매니저에게 연락해보자.\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: 이벤트 매니저 덕분에 모든 준비가 완료되었습니다! 휴!")


you = You()
you.askEventManager()
