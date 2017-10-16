BEGIN TRANSACTION;

/* Fix casing */
update anforande set parti = lower(parti);

/* Merge old and new parties */
update anforande set parti = "kd" where parti = "kds";
update anforande set parti = "l" where parti = "fp";

END TRANSACTION;
