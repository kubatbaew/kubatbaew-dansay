const items = document.querySelectorAll('.menu-item');

items.forEach(item => {
    item.addEventListener('click', () => {
        items.forEach(i => i.classList.remove('active'));
        item.classList.add('active');
    });
});


document.querySelectorAll('.menu-item button').forEach(button => {
    button.addEventListener('click', () => {
        const type = button.getAttribute('data-type');

        // Скрываем все блоки еды и интервальные блоки
        document.querySelectorAll('.food-block, .interval-blocks').forEach(block => {
            block.style.display = 'none';
        });

        // Убираем класс active у всех пунктов меню
        document.querySelectorAll('.menu-item').forEach(item => {
            item.classList.remove('active');
        });

        // Добавляем класс active текущему пункту меню
        button.parentElement.classList.add('active');

        if (type === 'all') {
            // Показываем все блоки еды и интервалы
            document.querySelectorAll('.food-block, .interval-blocks').forEach(block => {
                block.style.display = 'block';
            });
        } else {
            // Показываем только нужный блок еды и интервалы, если они рядом
            const targetBlocks = document.querySelectorAll(`.block-${type}`);
            targetBlocks.forEach(block => {
                block.style.display = 'block';

                // Показываем интервал перед или после, если есть
                const prev = block.previousElementSibling;
                const next = block.nextElementSibling;
                if (prev && prev.classList.contains('interval-blocks')) prev.style.display = 'block';
                if (next && next.classList.contains('interval-blocks')) next.style.display = 'block';
            });
        }
    });
});



const toggleButton = document.getElementById('theme-toggle');

function setTheme(theme) {
    document.body.classList.remove('light', 'dark');
    document.body.classList.add(theme);
    localStorage.setItem('theme', theme);
}

function toggleTheme() {
    const current = document.body.classList.contains('dark') ? 'dark' : 'light';
    setTheme(current === 'dark' ? 'light' : 'dark');
}

// Инициализация
document.addEventListener('DOMContentLoaded', () => {
    const saved = localStorage.getItem('theme') || 'light';
    setTheme(saved);
    toggleButton.addEventListener('click', toggleTheme);
});
