package artixbtw.higher_capped_horses.mixin;

import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;

import net.minecraft.world.entity.animal.equine.AbstractHorse;

@Mixin(AbstractHorse.class)
public class AbstractHorseHigherSpeedCapMixin {
	@Shadow
	@Final
	private static final float MAX_MOVEMENT_SPEED = (float) AbstractHorseAccessor.higherCappedHorses$invokeGenerateSpeed(() -> 2.241);
}
