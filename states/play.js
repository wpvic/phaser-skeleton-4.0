var play = function(){}

// FOR DEBUGGING PURPOSES, UNCOMMENT THE FOLLOWING LINE:
var obstacles = []

play.prototype = {
	create:function()
	{
		// RESETS SCORE TO 0
		score = 0
		// BG COLOR FOR THE GAME
		this.game.stage.backgroundColor = BG_COLOR

		this.frame_counter = 0
		this.physics.startSystem(Phaser.Physics.ARCADE)

		// obstacles group
		this.obstacles = this.game.add.group()
		
		// PLAYER
		this.player = this.game.add.sprite(this.game.width/2, 250, 'player')
		this.game.physics.enable(this.player, Phaser.Physics.ARCADE)
		this.player.jump_speed = -500
		this.player.enableBody = true
		this.player.body.collideWorldBounds = true
		this.player.anchor.setTo(.5,.5)

		// score SOUND
		this.sound.score = this.game.add.audio('score')
		this.sound.score.volume = .4

		this.sound.kill = this.game.add.audio('kill')

		// ADDING TEXT
		this.score = 0
		this.bmpText = this.game.add.bitmapText(this.game.width/2, 100, 'fontUsed', '', 150);
		this.bmpText.anchor.setTo(.5,.5)
		this.bmpText.scale.setTo(.3,.3)
		
		// support for mouse click and touchscreen input
		this.game.input.onDown.add(this.onDown, this)

		this.pauseAndUnpause(this.game)
		},

	update:function()
	{
		this.bmpText.text = score
		this.game.physics.arcade.overlap(this.player, this.obstacles, this.killOnContact, null, this)

		if(this.frame_counter%180 == 0)
		{
			this.spawnObstacle('obstacle', Math.random()*100, this.game.height, speed=200)
			this.spawnObstacle('obstacle', 200+Math.random()*100, this.game.height, speed=200)
			this.spawnObstacle('obstacle', 400+Math.random()*100, this.game.height, speed=200)
		}

		this.move()
		this.frame_counter++
	},

	spawnObstacle:function(entity,x,y,speed)
	{
		var obstacle = this.obstacles.create(x,y,entity)

		// UNCOMMENT FOR DEBUGGING
		obstacles.push(obstacle)

		this.game.physics.enable(obstacle, Phaser.Physics.ARCADE)

		obstacle.enableBody = true
		obstacle.body.colliderWorldBounds = true
		obstacle.body.immovable = true
		obstacle.anchor.setTo(.5,.5)
		obstacle.scale.setTo(1,1)
		obstacle.body.velocity.y = -speed
		obstacle.has_given_point = false

		obstacle.checkWorldBounds = true;
		obstacle.outOfBoundsKill = true;
	},

	scorePoint:function(obstacle)
	{
		if(obstacle.y < this.player.y && !obstacle.has_given_point)
		{
			score++
			this.sound.score.play()
			obstacle.has_given_point = true
		}
	},

	killOnContact:function(player,thing)
	{
		this.sound.kill.play()
		this.game.plugins.screenShake.shake(20);
		player.kill()
		this.game.state.start('gameOver')
	},

	// TAP ON TOUCHSCREEN OR CLICK WITH MOUSE
	onDown:function(pointer)
	{
	},

	// MOVE PLAYER
	move:function()
	{
		if(this.game.input.activePointer.isDown)
		{    
			this.player.body.velocity.x -= 35
			if(this.player.angle < 30)
			{
				this.player.angle += 2
			}
		}
		else
		{
			this.player.body.velocity.x += 35
			if(this.player.angle > -30)
			{
				this.player.angle -= 2
			}
		}
	},

	pauseAndUnpause:function(game)
	{
		var pause_button = this.game.add.sprite(this.game.width - 40, 40, 'pause')
		pause_button.anchor.setTo(.5,.5)
		pause_button.inputEnabled = true
		// pause:
		pause_button.events.onInputUp.add(
			function()
			{
				if(!game.paused)
				{
					game.paused = true
				}
				pause_watermark = this.game.add.sprite(this.game.width/2, this.game.height/2, 'pause')
				pause_watermark.anchor.setTo(.5,.5)
				pause_watermark.alpha = .1
			}, this)
		// unpause:
		game.input.onDown.add( 
			function()
			{
				if(game.paused)
				{
					game.paused = false
					pause_watermark.destroy()
				}
			} , self)
	},	
}

