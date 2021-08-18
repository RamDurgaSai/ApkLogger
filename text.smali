.class public final Lin/swiggy/deliveryapp/g/c;
.super Ljava/lang/Object;
.source "TaskEntityExtensions.kt"


# direct methods
.method public static final a(Lin/swiggy/deliveryapp/data/entities/TaskEntity;Lin/swiggy/deliveryapp/b/b/b;)Ljava/lang/String;
    .locals 2

    const-string v0, "$this$getLocationFromTask"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const-string v0, "firebaseRemoteConfig"

    invoke-static {p1, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 123
    invoke-interface {p1}, Lin/swiggy/deliveryapp/b/b/b;->ah()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    .line 124
    invoke-static {p0}, Lin/swiggy/deliveryapp/g/c;->h(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Ljava/lang/String;

    move-result-object p1

    goto :goto_0

    .line 126
    :cond_0
    invoke-interface {p1}, Lin/swiggy/deliveryapp/b/b/b;->aa()Z

    move-result p1

    if-eqz p1, :cond_1

    .line 127
    invoke-static {p0}, Lin/swiggy/deliveryapp/g/c;->g(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Ljava/lang/String;

    move-result-object p1

    goto :goto_0

    :cond_1
    move-object p1, v1

    :goto_0
    if-eqz p1, :cond_2

    goto :goto_1

    .line 131
    :cond_2
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->d()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_3

    const-string p1, "location"

    invoke-interface {p0, p1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    :cond_3
    invoke-static {v1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p1

    :goto_1
    return-object p1
.end method

.method public static final a(Ljava/util/List;Ljava/util/Set;)Ljava/util/List;
    .locals 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List<",
            "Lin/swiggy/deliveryapp/data/entities/TaskEntity;",
            ">;",
            "Ljava/util/Set<",
            "Ljava/lang/Long;",
            ">;)",
            "Ljava/util/List<",
            "Ljava/lang/Long;",
            ">;"
        }
    .end annotation

    const-string v0, "$this$getShallowAndDirtyTasks"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const-string v0, "shallowJobLegs"

    invoke-static {p1, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 25
    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    check-cast v0, Ljava/util/List;

    .line 26
    check-cast p0, Ljava/lang/Iterable;

    .line 212
    invoke-interface {p0}, Ljava/lang/Iterable;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :cond_0
    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lin/swiggy/deliveryapp/data/entities/TaskEntity;

    .line 27
    invoke-virtual {v1}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->h()J

    move-result-wide v2

    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v2

    invoke-interface {p1, v2}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_0

    .line 28
    invoke-static {v1}, Lin/swiggy/deliveryapp/g/c;->c(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z

    move-result v2

    if-nez v2, :cond_1

    invoke-static {v1}, Lin/swiggy/deliveryapp/g/c;->b(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z

    move-result v2

    if-eqz v2, :cond_0

    .line 29
    :cond_1
    invoke-virtual {v1}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->a()J

    move-result-wide v1

    invoke-static {v1, v2}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v1

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_2
    return-object v0
.end method

.method public static final a(Ljava/util/List;)Ljava/util/Map;
    .locals 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List<",
            "Lin/swiggy/deliveryapp/data/entities/TaskEntity;",
            ">;)",
            "Ljava/util/Map<",
            "Ljava/lang/Long;",
            "Lin/swiggy/deliveryapp/data/entities/TaskEntity;",
            ">;"
        }
    .end annotation

    const-string v0, "$this$toMap"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 43
    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    check-cast v0, Ljava/util/Map;

    .line 44
    check-cast p0, Ljava/lang/Iterable;

    .line 214
    invoke-interface {p0}, Ljava/lang/Iterable;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lin/swiggy/deliveryapp/data/entities/TaskEntity;

    .line 45
    invoke-virtual {v1}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->a()J

    move-result-wide v2

    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v2

    invoke-interface {v0, v2, v1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    :cond_0
    return-object v0
.end method

.method public static final a(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 2

    const-string v0, "$this$isPending"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 17
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->b()Ljava/lang/String;

    move-result-object p0

    const/4 v0, 0x1

    const-string v1, "COMPLETED"

    invoke-static {v1, p0, v0}, Lkotlin/j/g;->a(Ljava/lang/String;Ljava/lang/String;Z)Z

    move-result p0

    xor-int/2addr p0, v0

    return p0
.end method

.method public static final b(Lin/swiggy/deliveryapp/data/entities/TaskEntity;Lin/swiggy/deliveryapp/b/b/b;)Lcom/google/android/gms/maps/model/LatLng;
    .locals 6

    const-string v0, "$this$getLatLng"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const-string v0, "swiggyFirebaseRemoteConfig"

    invoke-static {p1, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 161
    invoke-static {p0, p1}, Lin/swiggy/deliveryapp/g/c;->a(Lin/swiggy/deliveryapp/data/entities/TaskEntity;Lin/swiggy/deliveryapp/b/b/b;)Ljava/lang/String;

    move-result-object p0

    move-object v0, p0

    check-cast v0, Ljava/lang/CharSequence;

    const-string p0, ","

    filled-new-array {p0}, [Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x0

    const/4 v3, 0x0

    const/4 v4, 0x6

    const/4 v5, 0x0

    invoke-static/range {v0 .. v5}, Lkotlin/j/g;->b(Ljava/lang/CharSequence;[Ljava/lang/String;ZIILjava/lang/Object;)Ljava/util/List;

    move-result-object p0

    if-eqz p0, :cond_0

    const/4 p1, 0x0

    .line 163
    invoke-interface {p0, p1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Ljava/lang/String;

    invoke-static {p1}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D

    move-result-wide v0

    const/4 p1, 0x1

    .line 164
    invoke-interface {p0, p1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/lang/String;

    invoke-static {p0}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D

    move-result-wide p0

    .line 165
    new-instance v2, Lcom/google/android/gms/maps/model/LatLng;

    invoke-direct {v2, v0, v1, p0, p1}, Lcom/google/android/gms/maps/model/LatLng;-><init>(DD)V

    return-object v2

    :cond_0
    const/4 p0, 0x0

    return-object p0
.end method

.method public static final b(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 5

    const-string v0, "$this$isDirty"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 21
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->f()Ljava/lang/Long;

    move-result-object v0

    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->g()J

    move-result-wide v1

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {v0}, Ljava/lang/Long;->longValue()J

    move-result-wide v3

    cmp-long p0, v3, v1

    if-eqz p0, :cond_1

    :goto_0
    const/4 p0, 0x1

    goto :goto_1

    :cond_1
    const/4 p0, 0x0

    :goto_1
    return p0
.end method

.method public static final c(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isShallow"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 37
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->e()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_1

    .line 38
    invoke-interface {p0}, Ljava/util/Map;->isEmpty()Z

    move-result p0

    if-eqz p0, :cond_0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    goto :goto_1

    :cond_1
    :goto_0
    const/4 p0, 0x1

    :goto_1
    return p0
.end method

.method public static final c(Lin/swiggy/deliveryapp/data/entities/TaskEntity;Lin/swiggy/deliveryapp/b/b/b;)Z
    .locals 6

    const-string v0, "$this$hasValidLocation"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const-string v0, "swiggyFirebaseRemoteConfig"

    invoke-static {p1, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 188
    invoke-static {p0, p1}, Lin/swiggy/deliveryapp/g/c;->a(Lin/swiggy/deliveryapp/data/entities/TaskEntity;Lin/swiggy/deliveryapp/b/b/b;)Ljava/lang/String;

    move-result-object p0

    .line 189
    move-object v0, p0

    check-cast v0, Ljava/lang/CharSequence;

    const-string p0, ","

    filled-new-array {p0}, [Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x0

    const/4 v3, 0x0

    const/4 v4, 0x6

    const/4 v5, 0x0

    invoke-static/range {v0 .. v5}, Lkotlin/j/g;->b(Ljava/lang/CharSequence;[Ljava/lang/String;ZIILjava/lang/Object;)Ljava/util/List;

    move-result-object p0

    if-eqz p0, :cond_0

    .line 190
    invoke-interface {p0}, Ljava/util/List;->size()I

    move-result p0

    const/4 p1, 0x2

    if-ne p0, p1, :cond_0

    const/4 p0, 0x1

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    :goto_0
    return p0
.end method

.method public static final d(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isTaskInProgress"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 113
    invoke-static {p0}, Lin/swiggy/deliveryapp/g/c;->a(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->i()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_0

    const-string v0, "inProgress"

    invoke-interface {p0, v0}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    :goto_0
    invoke-static {p0}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    check-cast p0, Ljava/lang/CharSequence;

    const-string v0, "true"

    check-cast v0, Ljava/lang/CharSequence;

    invoke-static {p0, v0}, Lorg/apache/commons/lang3/StringUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    if-eqz p0, :cond_1

    const/4 p0, 0x1

    goto :goto_1

    :cond_1
    const/4 p0, 0x0

    :goto_1
    return p0
.end method

.method public static final e(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isPickUpTask"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 116
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->c()Ljava/lang/String;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object p0

    const-string v0, "(this as java.lang.String).toUpperCase()"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->a(Ljava/lang/Object;Ljava/lang/String;)V

    check-cast p0, Ljava/lang/CharSequence;

    const-string v0, "PICK_UP"

    check-cast v0, Ljava/lang/CharSequence;

    invoke-static {p0, v0}, Lorg/apache/commons/lang3/StringUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    return p0

    :cond_0
    new-instance p0, Lkotlin/TypeCastException;

    const-string v0, "null cannot be cast to non-null type java.lang.String"

    invoke-direct {p0, v0}, Lkotlin/TypeCastException;-><init>(Ljava/lang/String;)V

    throw p0
.end method

.method public static final f(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isDropTask"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 119
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->c()Ljava/lang/String;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object p0

    const-string v0, "(this as java.lang.String).toUpperCase()"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->a(Ljava/lang/Object;Ljava/lang/String;)V

    check-cast p0, Ljava/lang/CharSequence;

    const-string v0, "DROP"

    check-cast v0, Ljava/lang/CharSequence;

    invoke-static {p0, v0}, Lorg/apache/commons/lang3/StringUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p0

    return p0

    :cond_0
    new-instance p0, Lkotlin/TypeCastException;

    const-string v0, "null cannot be cast to non-null type java.lang.String"

    invoke-direct {p0, v0}, Lkotlin/TypeCastException;-><init>(Ljava/lang/String;)V

    throw p0
.end method

.method public static final g(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Ljava/lang/String;
    .locals 2

    const-string v0, "$this$getSuggestedAddress"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const/4 v0, 0x0

    .line 139
    :try_start_0
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->d()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_0

    const-string v1, "metaData"

    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    :cond_0
    move-object p0, v0

    :goto_0
    instance-of v1, p0, Ljava/util/Map;

    if-nez v1, :cond_1

    move-object p0, v0

    :cond_1
    check-cast p0, Ljava/util/Map;

    if-eqz p0, :cond_2

    const-string v1, "suggestedAddressData"

    .line 140
    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_1

    :cond_2
    move-object p0, v0

    :goto_1
    instance-of v1, p0, Ljava/util/Map;

    if-nez v1, :cond_3

    move-object p0, v0

    :cond_3
    check-cast p0, Ljava/util/Map;

    if-eqz p0, :cond_4

    const-string v1, "location"

    .line 141
    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_2

    :cond_4
    move-object p0, v0

    :goto_2
    instance-of v1, p0, Ljava/lang/String;

    if-nez v1, :cond_5

    move-object p0, v0

    :cond_5
    check-cast p0, Ljava/lang/String;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_3

    :catch_0
    move-object p0, v0

    :goto_3
    return-object p0
.end method

.method public static final h(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Ljava/lang/String;
    .locals 2

    const-string v0, "$this$getSharedAddress"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const/4 v0, 0x0

    .line 152
    :try_start_0
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->d()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_0

    const-string v1, "metaData"

    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    :cond_0
    move-object p0, v0

    :goto_0
    instance-of v1, p0, Ljava/util/Map;

    if-nez v1, :cond_1

    move-object p0, v0

    :cond_1
    check-cast p0, Ljava/util/Map;

    if-eqz p0, :cond_2

    const-string v1, "sharedLocationData"

    .line 153
    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_1

    :cond_2
    move-object p0, v0

    :goto_1
    instance-of v1, p0, Ljava/util/Map;

    if-nez v1, :cond_3

    move-object p0, v0

    :cond_3
    check-cast p0, Ljava/util/Map;

    if-eqz p0, :cond_4

    const-string v1, "location"

    .line 154
    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_2

    :cond_4
    move-object p0, v0

    :goto_2
    instance-of v1, p0, Ljava/lang/String;

    if-nez v1, :cond_5

    move-object p0, v0

    :cond_5
    check-cast p0, Ljava/lang/String;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_3

    :catch_0
    move-object p0, v0

    :goto_3
    return-object p0
.end method

.method public static final i(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Ljava/lang/String;
    .locals 2

    const-string v0, "$this$getRestaurantIdFromTask"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const/4 v0, 0x0

    .line 172
    :try_start_0
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->d()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_0

    const-string v1, "metaData"

    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    :cond_0
    move-object p0, v0

    :goto_0
    check-cast p0, Ljava/util/Map;

    if-eqz p0, :cond_1

    const-string v1, "referenceId"

    .line 173
    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_1

    :cond_1
    move-object p0, v0

    :goto_1
    if-eqz p0, :cond_2

    check-cast p0, Ljava/lang/String;

    return-object p0

    :cond_2
    new-instance p0, Lkotlin/TypeCastException;

    const-string v1, "null cannot be cast to non-null type kotlin.String"

    invoke-direct {p0, v1}, Lkotlin/TypeCastException;-><init>(Ljava/lang/String;)V

    throw p0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    .line 171
    :catch_0
    check-cast v0, Ljava/lang/String;

    return-object v0
.end method

.method public static final j(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Ljava/lang/String;
    .locals 2

    const-string v0, "$this$getRestaurantName"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    const/4 v0, 0x0

    .line 181
    :try_start_0
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->d()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_0

    const-string v1, "name"

    invoke-interface {p0, v1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    :cond_0
    move-object p0, v0

    :goto_0
    if-eqz p0, :cond_1

    check-cast p0, Ljava/lang/String;

    return-object p0

    :cond_1
    new-instance p0, Lkotlin/TypeCastException;

    const-string v1, "null cannot be cast to non-null type kotlin.String"

    invoke-direct {p0, v1}, Lkotlin/TypeCastException;-><init>(Ljava/lang/String;)V

    throw p0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    .line 180
    :catch_0
    check-cast v0, Ljava/lang/String;

    return-object v0
.end method

.method public static final k(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isCreated"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 194
    invoke-static {p0}, Lin/swiggy/deliveryapp/g/c;->c(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z

    move-result v0

    if-nez v0, :cond_0

    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->b()Ljava/lang/String;

    move-result-object p0

    const-string v0, "CREATED"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->a(Ljava/lang/Object;Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    :goto_0
    return p0
.end method

.method public static final l(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isArrived"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 198
    invoke-static {p0}, Lin/swiggy/deliveryapp/g/c;->c(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z

    move-result v0

    if-nez v0, :cond_0

    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->b()Ljava/lang/String;

    move-result-object p0

    const-string v0, "ARRIVED"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->a(Ljava/lang/Object;Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    :goto_0
    return p0
.end method

.method public static final m(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isCompleted"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 202
    invoke-static {p0}, Lin/swiggy/deliveryapp/g/c;->c(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z

    move-result v0

    if-nez v0, :cond_0

    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->b()Ljava/lang/String;

    move-result-object p0

    const-string v0, "COMPLETED"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->a(Ljava/lang/Object;Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    :goto_0
    return p0
.end method

.method public static final n(Lin/swiggy/deliveryapp/data/entities/TaskEntity;)Z
    .locals 1

    const-string v0, "$this$isAddressVerified"

    invoke-static {p0, v0}, Lkotlin/e/b/m;->c(Ljava/lang/Object;Ljava/lang/String;)V

    .line 206
    invoke-virtual {p0}, Lin/swiggy/deliveryapp/data/entities/TaskEntity;->d()Ljava/util/Map;

    move-result-object p0

    if-eqz p0, :cond_0

    const-string v0, "isVerified"

    invoke-interface {p0, v0}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    :goto_0
    const/4 v0, 0x1

    invoke-static {v0}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v0

    invoke-static {p0, v0}, Lkotlin/e/b/m;->a(Ljava/lang/Object;Ljava/lang/Object;)Z

    move-result p0

    return p0
.end method