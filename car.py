<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>三维迪士尼极速光轮</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #000;
            font-family: Arial, sans-serif;
        }
        
        #gameContainer {
            position: relative;
            width: 100vw;
            height: 100vh;
        }
        
        #gameCanvas {
            display: block;
        }
        
        #uiContainer {
            position: absolute;
            top: 20px;
            left: 20px;
            color: white;
            z-index: 10;
        }
        
        #startScreen {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            z-index: 20;
        }
        
        #startButton {
            margin-top: 20px;
            padding: 15px 30px;
            font-size: 18px;
            background-color: #ff69b4;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            color: white;
            font-weight: bold;
        }
        
        #gameOverScreen {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            z-index: 20;
        }
        
        #restartButton {
            margin-top: 20px;
            padding: 15px 30px;
            font-size: 18px;
            background-color: #ff69b4;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            color: white;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="gameContainer">
        <canvas id="gameCanvas"></canvas>
        
        <div id="uiContainer">
            <div>速度: <span id="speedDisplay">0</span> km/h</div>
            <div>分数: <span id="scoreDisplay">0</span></div>
            <div>时间: <span id="timeDisplay">0</span>s</div>
        </div>
        
        <div id="startScreen">
            <h1>三维迪士尼极速光轮</h1>
            <p>使用方向键控制光轮赛车</p>
            <p>避开障碍物，获得高分！</p>
            <button id="startButton">开始游戏</button>
        </div>
        
        <div id="gameOverScreen">
            <h1>游戏结束</h1>
            <p>最终分数: <span id="finalScore">0</span></p>
            <button id="restartButton">重新开始</button>
        </div>
    </div>

    <script>
        // 游戏变量
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const startScreen = document.getElementById('startScreen');
        const gameOverScreen = document.getElementById('gameOverScreen');
        const startButton = document.getElementById('startButton');
        const restartButton = document.getElementById('restartButton');
        const speedDisplay = document.getElementById('speedDisplay');
        const scoreDisplay = document.getElementById('scoreDisplay');
        const timeDisplay = document.getElementById('timeDisplay');
        const finalScore = document.getElementById('finalScore');
        
        // 设置画布大小
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
        
        // 游戏状态
        let gameRunning = false;
        let playerX = 0;
        let playerY = 0;
        let playerSpeed = 0;
        let maxSpeed = 20;
        let acceleration = 0.2;
        let deceleration = 0.1;
        let turnSpeed = 0.05;
        let obstacles = [];
        let score = 0;
        let gameTime = 0;
        let lastTime = 0;
        let keys = {};
        
        // 初始化游戏
        function initGame() {
            playerX = 0;
            playerY = 0;
            playerSpeed = 0;
            obstacles = [];
            score = 0;
            gameTime = 0;
            lastTime = performance.now();
            
            // 创建初始障碍物
            for (let i = 0; i < 10; i++) {
                spawnObstacle(i * 100);
            }
        }
        
        // 生成障碍物
        function spawnObstacle(zOffset = 0) {
            const z = -500 - Math.random() * 1000 - zOffset;
            const x = (Math.random() - 0.5) * 400;
            const y = (Math.random() - 0.5) * 200;
            const size = 20 + Math.random() * 30;
            
            obstacles.push({
                x: x,
                y: y,
                z: z,
                size: size,
                type: Math.floor(Math.random() * 3) // 0-2 不同类型障碍物
            });
        }
        
        // 更新游戏状态
        function update(deltaTime) {
            // 加速/减速
            if (keys['ArrowUp']) {
                playerSpeed = Math.min(playerSpeed + acceleration, maxSpeed);
            } else if (keys['ArrowDown']) {
                playerSpeed = Math.max(playerSpeed - acceleration, -maxSpeed/2);
            } else {
                // 自然减速
                if (playerSpeed > 0) {
                    playerSpeed = Math.max(playerSpeed - deceleration, 0);
                } else if (playerSpeed < 0) {
                    playerSpeed = Math.min(playerSpeed + deceleration, 0);
                }
            }
            
            // 转向
            if (keys['ArrowLeft']) {
                playerX -= turnSpeed * playerSpeed * 10;
            }
            if (keys['ArrowRight']) {
                playerX += turnSpeed * playerSpeed * 10;
            }
            if (keys['ArrowUp'] || keys['ArrowDown']) {
                playerY -= turnSpeed * playerSpeed * 5;
            }
            
            // 限制玩家移动范围
            playerX = Math.max(-200, Math.min(200, playerX));
            playerY = Math.max(-150, Math.min(150, playerY));
            
            // 更新障碍物位置（模拟前进）
            for (let i = 0; i < obstacles.length; i++) {
                obstacles[i].z += playerSpeed * deltaTime * 0.5;
                
                // 如果障碍物经过玩家，移除并生成新的
                if (obstacles[i].z > 50) {
                    obstacles.splice(i, 1);
                    spawnObstacle();
                    score += 10;
                    i--;
                }
            }
            
            // 检查碰撞
            for (let i = 0; i < obstacles.length; i++) {
                const obstacle = obstacles[i];
                const dx = obstacle.x - playerX;
                const dy = obstacle.y - playerY;
                const dz = obstacle.z - 0; // 玩家z位置为0
                const distance = Math.sqrt(dx*dx + dy*dy + dz*dz);
                
                if (distance < obstacle.size/2 + 15) { // 假设玩家半径为15
                    gameOver();
                    return;
                }
            }
            
            // 保持足够的障碍物
            if (obstacles.length < 15) {
                spawnObstacle(1000);
            }
            
            // 更新时间
            gameTime += deltaTime / 1000;
            
            // 更新UI
            speedDisplay.textContent = Math.round(playerSpeed * 10);
            scoreDisplay.textContent = Math.round(score);
            timeDisplay.textContent = Math.round(gameTime);
        }
        
        // 绘制游戏画面
        function draw() {
            // 清空画布
            ctx.fillStyle = '#000';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // 绘制背景网格（模拟赛道）
            drawGrid();
            
            // 投影变换函数
            function project(x, y, z) {
                // 简单的透视投影
                const scale = 500 / (500 + z);
                const projectedX = canvas.width/2 + (x * scale);
                const projectedY = canvas.height/2 + (y * scale);
                return { x: projectedX, y: projectedY, scale: scale };
            }
            
            // 绘制障碍物
            for (let i = 0; i < obstacles.length; i++) {
                const obstacle = obstacles[i];
                if (obstacle.z > -500) { // 只绘制在视野内的物体
                    const pos = project(obstacle.x, obstacle.y, obstacle.z);
                    
                    if (pos.scale > 0) { // 只绘制在前方的物体
                        ctx.save();
                        
                        // 根据类型绘制不同颜色的障碍物
                        switch(obstacle.type) {
                            case 0:
                                ctx.fillStyle = '#ff5252'; // 红色
                                break;
                            case 1:
                                ctx.fillStyle = '#448aff'; // 蓝色
                                break;
                            case 2:
                                ctx.fillStyle = '#69f0ae'; // 绿色
                                break;
                        }
                        
                        // 绘制障碍物
                        ctx.beginPath();
                        ctx.arc(pos.x, pos.y, obstacle.size * pos.scale, 0, Math.PI * 2);
                        ctx.fill();
                        
                        // 添加发光效果
                        ctx.shadowColor = ctx.fillStyle;
                        ctx.shadowBlur = 15 * pos.scale;
                        ctx.fill();
                        ctx.shadowBlur = 0;
                        
                        ctx.restore();
                    }
                }
            }
            
            // 绘制玩家（光轮赛车）
            const playerPos = project(playerX, playerY, 0);
            ctx.save();
            ctx.fillStyle = '#ffffff';
            ctx.beginPath();
            ctx.arc(playerPos.x, playerPos.y, 20, 0, Math.PI * 2);
            ctx.fill();
            
            // 光环效果
            ctx.strokeStyle = '#448aff';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.arc(playerPos.x, playerPos.y, 25, 0, Math.PI * 2);
            ctx.stroke();
            
            // 尾焰效果
            ctx.fillStyle = '#ffeb3b';
            ctx.globalAlpha = 0.7;
            ctx.beginPath();
            ctx.ellipse(playerPos.x, playerPos.y + 20, 8, 15, Math.PI/2, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.restore();
        }
        
        // 绘制背景网格
        function drawGrid() {
            ctx.strokeStyle = 'rgba(100, 100, 255, 0.2)';
            ctx.lineWidth = 1;
            
            // 绘制纵向线
            for (let x = -200; x <= 200; x += 50) {
                for (let z = -500; z < 1000; z += 100) {
                    const p1 = project(x, -200, z);
                    const p2 = project(x, 200, z);
                    
                    if (p1.scale > 0 && p2.scale > 0) {
                        ctx.beginPath();
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.stroke();
                    }
                }
            }
            
            // 绘制横向线
            for (let y = -200; y <= 200; y += 50) {
                for (let z = -500; z < 1000; z += 100) {
                    const p1 = project(-200, y, z);
                    const p2 = project(200, y, z);
                    
                    if (p1.scale > 0 && p2.scale > 0) {
                        ctx.beginPath();
                        ctx.moveTo(p1.x, p1.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.stroke();
                    }
                }
            }
        }
        
        // 游戏主循环
        function gameLoop(timestamp) {
            if (!gameRunning) return;
            
            const deltaTime = timestamp - lastTime;
            lastTime = timestamp;
            
            update(deltaTime);
            draw();
            
            requestAnimationFrame(gameLoop);
        }
        
        // 开始游戏
        function startGame() {
            initGame();
            gameRunning = true;
            startScreen.style.display = 'none';
            lastTime = performance.now();
            requestAnimationFrame(gameLoop);
        }
        
        // 结束游戏
        function gameOver() {
            gameRunning = false;
            finalScore.textContent = Math.round(score);
            gameOverScreen.style.display = 'flex';
        }
        
        // 重新开始游戏
        function restartGame() {
            gameOverScreen.style.display = 'none';
            startGame();
        }
        
        // 键盘事件监听
        window.addEventListener('keydown', (e) => {
            keys[e.key] = true;
        });
        
        window.addEventListener('keyup', (e) => {
            keys[e.key] = false;
        });
        
        // 按钮事件监听
        startButton.addEventListener('click', startGame);
        restartButton.addEventListener('click', restartGame);
        
        // 初始绘制
        draw();
    </script>
</body>
</html>
 
    
  
