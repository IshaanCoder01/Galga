def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Missile
    """), SpacePlane, 200, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Bogey: Sprite = None
projectile: Sprite = None
SpacePlane: Sprite = None
SpacePlane = sprites.create(assets.image("""
    Spaceplane
"""), SpriteKind.player)
controller.move_sprite(SpacePlane, 200, 200)
info.set_life(3)
SpacePlane.set_stay_in_screen(True)

def on_update_interval():
    global Bogey
    Bogey = sprites.create(assets.image("""
        Bogey
    """), SpriteKind.enemy)
    Bogey.set_velocity(-100, 0)
    Bogey.set_position(160, randint(5, 115))
    Bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
