import cv2 as cv

def video_read_save():
    # 创建视频，读取/捕获对象
    videoRead = "../../statics/images/Vid01.mp4"
    capRead = cv.VideoCapture(videoRead)

    # 设置写入视频图像的高、宽、帧速率和总帧数
    width = int(capRead.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(capRead.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = round(capRead.get(cv.CAP_PROP_FPS))
    frame_count = int(capRead.get(cv.CAP_PROP_FRAME_COUNT))
    print(height, width, fps, frame_count)

    # 创建视频写入对象
    fourcc = cv.VideoWriter.fourcc(*'XVID')
    videoWriter = "../../vid03.avi"
    capWriter = cv.VideoWriter(videoWriter, fourcc, fps, (width, height))

    # 读取视频文件，抽帧写入视频文件
    frameNum = 0  # 视频帧数初值
    timef= 30  # 设置抽帧间隔
    while capRead.isOpened():  # 检查视频捕获是否成功
        ret, frame = capRead.read()  # 读取下一帧视频图像
        if ret is True:
            frameNum = frameNum + 1
            cv.imshow('videoRead', frame)
            if frameNum % timef == 0:
                capWriter.write(frame)  # 将当前帧写入文件
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print(frameNum)
            break
    capRead.release()
    capWriter.release()
    cv.destroyAllWindows()

def camera_read_save():
    # 创建视频捕获对象，调用笔记本摄像头
    # cam = cv.VideoCapture(0)  # 创建捕获对象，0 为笔记本摄像头
    cam = cv.VideoCapture(0, cv.CAP_DSHOW)  # 修改 API 设置为视频输入 DirectShow

    # 设置写入视频图像的高，宽，帧速率和总帧数
    fps = 20  # 设置帧速率
    width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))  # 640
    height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))  # 480
    fourcc = cv.VideoWriter.fourcc(*'XVID')  # 编码器设置 XVID
    # 创建写入视频对象
    videoPath = "../../camera.avi"  # 写入视频文件的路径
    capWrite = cv.VideoWriter(videoPath, fourcc, fps, (width, height))
    print(fourcc, fps, (width, height))


    sn = 0  # 抓拍图像编号
    while cam.isOpened():  # 检查视频捕获是否成功
        success, frame = cam.read()  # 读取下一帧视频图像
        if success is True:
            cv.imshow('video', frame)  # 播放视频图像
            capWrite.write(frame)  # 将当前帧写入视频文件
            key = cv.waitKey(1) & 0xFF  # 接收键盘输入
            if key == ord('c'):  # 按 'c' 键抓拍当前帧
                filePath = "../../statics/images/cam/photo{:d}.png".format(sn)  # 保存文件名
                cv.imwrite(filePath, frame)  # 将当前帧保存为图片
                sn += 1  # 更新写入图像编号
                print(filePath)
            elif key == ord('q'):  # 按 'q' 键结束录制视频
                break
        else:
            print("Can't receive frame.")
            break

    cam.release()  # 关闭视频捕获对象
    capWrite.release()  # 关闭视频写入对象
    cv.destroyAllWindows()  # 关闭显示窗口

if __name__ == '__main__':
    # video_read_save()
    camera_read_save()