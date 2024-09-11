
    const videoElement = document.getElementById('myVideo');
    const buttonContainer = document.getElementById('buttonContainer');

    // Устанавливаем время, когда кнопки появятся (например, 5 секунд)
    const showButtonsAt = 5; // Время в секундах

    videoElement.addEventListener('timeupdate', function() {
        if (videoElement.currentTime >= showButtonsAt) {
            buttonContainer.style.display = 'flex'; // Показываем кнопки
        } else {
            buttonContainer.style.display = 'none'; // Скрываем кнопки
        }
    });

    function changeVideo(video) {
        videoElement.src = video;
        videoElement.play();
        buttonContainer.style.display = 'none'; // Скрываем кнопки после выбора видео
    }
