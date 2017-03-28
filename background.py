import pygame, random, cloud, ground

class Background:

    def __init__(self, height, width):
        self.cloud_types = [pygame.image.load("images/cloud1.png"),
                            pygame.image.load("images/cloud2.png"),
                            pygame.image.load("images/cloud3.png")]
        self.screen_width = width
        self.screen_height = height
        self.clouds = []
        self.ground = ground.Ground(width, height)

    def paint_back_clouds(self, surface):
        for cloud in self.clouds:
            if cloud.front_back == "back":
                cloud.paint(surface)

    def paint_front_clouds(self, surface):
        for cloud in self.clouds:
            if cloud.front_back == "front":
                cloud.paint(surface)

    def paint_ground(self, surface):
        self.ground.paint(surface)


    def add_cloud(self):
        temp = random.randint(1,100)
        if temp > 96 or len(self.clouds) == 0:
            if temp > 99:
                front_back = 'front'
            else:
                front_back = 'back'
            cloud_type = random.choice(self.cloud_types)
            self.clouds.append(cloud.Cloud(self.screen_width, self.screen_height, cloud_type, front_back))



    def move_clouds(self):
        self.add_cloud()
        deletable_clouds = []
        for index, cloud in enumerate(self.clouds):
            deletable = cloud.move()
            if deletable:
                deletable_clouds.append(index)
        deletable_clouds = sorted(deletable_clouds, reverse=True)
        if len(deletable_clouds) > 0:
            self.delete_cloud(deletable_clouds)

    def delete_cloud(self, clouds_i):
        for i in clouds_i:
            self.clouds.pop(i)
