controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(assets.image`
        Missile
    `, SpacePlane, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.fire, 500)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    scene.cameraShake(4, 500)
    info.changeLifeBy(-1)
})
let Bogey : Sprite = null
let projectile : Sprite = null
let SpacePlane : Sprite = null
SpacePlane = sprites.create(assets.image`
    Spaceplane
`, SpriteKind.Player)
controller.moveSprite(SpacePlane, 200, 200)
info.setLife(3)
SpacePlane.setStayInScreen(true)
game.onUpdateInterval(500, function on_update_interval() {
    
    Bogey = sprites.create(assets.image`
        Bogey
    `, SpriteKind.Enemy)
    Bogey.setVelocity(-100, 0)
    Bogey.setPosition(160, randint(5, 115))
    Bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
