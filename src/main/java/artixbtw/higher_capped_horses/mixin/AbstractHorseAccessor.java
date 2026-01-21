package artixbtw.higher_capped_horses.mixin;

import java.util.function.DoubleSupplier;

import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.gen.Invoker;

import net.minecraft.world.entity.animal.equine.AbstractHorse;

@Mixin(AbstractHorse.class)
public interface AbstractHorseAccessor {
	@Invoker("generateSpeed")
	static double higherCappedHorses$invokeGenerateSpeed(DoubleSupplier supplier) {
		throw new AssertionError();
	}
}
