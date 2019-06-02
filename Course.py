from Wall import WallSprite
from Car import CarSprite
from Trophy import TrophySprite

Map1 = (
    [
        WallSprite((512, 2.5), 1024, 5),
        WallSprite((512, 765.5), 1024, 5),
        WallSprite((2.5, 384), 5, 768),
        WallSprite((1021.5, 384), 5, 768),
        WallSprite((113 * 1, 768 - 130), 5, 260),
        WallSprite((113 * 2, 768 - 230), 5, 260),
        WallSprite((113 * 3, 768 - 130), 5, 260),
        WallSprite((113 * 4, 768 - 230), 5, 260),
        WallSprite((113 * 5, 768 - 130), 5, 260),
        WallSprite((113 * 6, 768 - 230), 5, 260),
        WallSprite((113 * 7, 768 - 130), 5, 260),
        WallSprite((113 * 8, 768 - 230), 5, 260),
        WallSprite((113 * 4, 768 - 360), 113 * 8, 5),
        WallSprite((1024 - 113 * 4, 768 - 490), 113 * 8, 5),
        WallSprite((1024 - 113 * 4, 130), 113 * 8, 5),
        WallSprite((120 , 204), 5, 152),
    ],
    [
        TrophySprite((950,45))
    ],
    CarSprite('images/car.png', (50, 700))
)

Map2 = (
    None, None, None
)

Map3 = (
    None, None, None
)