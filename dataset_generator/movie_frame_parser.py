import os.path

import cv2


def extractFramesFromMovie(fileName: str):
    root = os.path.dirname(__file__)
    print('root is :', root)

    capture = cv2.VideoCapture(fileName)
    file = fileName.split('\\')[-1]
    frameCount = 1
    totalFramecount = 1

    framesPath = os.path.join(root, 'frames\\frames_{0}'.format(file))
    print('framesPath is: ', framesPath)

    if not os.path.exists(framesPath):
        os.makedirs(framesPath)

    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break
        if frameCount % 96 == 0:
            framePath = framesPath + '\\frames_{0}.jpg'.format(totalFramecount)
            cv2.imwrite(framePath, frame)
            totalFramecount += 1
        frameCount += 1

    return totalFramecount


def main():
    moviesRoot = os.path.dirname(__file__) + '\\movies'
    print(moviesRoot)

    for movie in os.listdir(moviesRoot):
        print('Begin extracting frames for : %s' % movie)
        moviePath = f'{moviesRoot}\\{movie}'
        extractedFrameCount = extractFramesFromMovie(moviePath)
        print(f'Done extracting frames for : {movie}\n'
              f'Extracted frames : {extractedFrameCount}')
        print('--------------------')

main()
