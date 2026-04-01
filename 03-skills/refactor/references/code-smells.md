# 代码坏味道目录

基于 Martin Fowler《重构》（第 2 版）整理的代码坏味道参考。代码坏味道是更深层问题的外在表现——提示你的设计可能存在问题。

> 「代码坏味道是一种表面迹象，通常对应系统中更深层的问题。」—— Martin Fowler

---

## 臃肿（Bloaters）

表示某段代码已经膨胀到难以有效应对的坏味道。

### 过长函数（Long Method）

**迹象：**
- 函数超过约 30～50 行
- 需要滚动才能看完整个函数
- 嵌套层级多
- 用注释说明每一段在做什么

**为何不好：**
- 难以理解
- 难以单独测试
- 修改容易产生意外影响
- 重复逻辑藏在内部

**重构手法：**
- Extract Method
- Replace Temp with Query
- Introduce Parameter Object
- Replace Method with Method Object
- Decompose Conditional

**示例（重构前）：**
```javascript
function processOrder(order) {
  // Validate order (20 lines)
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... more validation

  // Calculate totals (30 lines)
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... tax, shipping, discounts

  // Send notifications (20 lines)
  // ... email logic
}
```

**示例（重构后）：**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### 过大的类（Large Class）

**迹象：**
- 实例变量很多（多于约 7～10 个）
- 方法很多（多于约 15～20 个）
- 类名含糊（Manager、Handler、Processor）
- 方法并未使用全部实例变量

**为何不好：**
- 违背单一职责原则
- 难以测试
- 改动会波及无关功能
- 难以复用其中一部分

**重构手法：**
- Extract Class
- Extract Subclass
- Extract Interface

**识别：**
```
Lines of code > 300
Number of methods > 15
Number of fields > 10
```

---

### 基本类型偏执（Primitive Obsession）

**迹象：**
- 用基本类型表达领域概念（如用 string 表示邮箱、用 int 表示金额）
- 用基本类型数组代替对象
- 用字符串常量表示类型码
- 魔法数字 / 魔法字符串

**为何不好：**
- 类型层面无法校验
- 逻辑散落在各处
- 容易传错值
- 缺少领域概念

**重构手法：**
- Replace Primitive with Object
- Replace Type Code with Class
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**示例（重构前）：**
```javascript
const user = {
  email: 'john@example.com',     // Just a string
  phone: '1234567890',           // Just a string
  status: 'active',              // Magic string
  balance: 10050                 // Cents as integer
};
```

**示例（重构后）：**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### 过长参数列（Long Parameter List）

**迹象：**
- 参数达到 4 个或以上
- 总是一起出现的参数
- 用布尔标志改变函数行为
- 经常传入 null/undefined

**为何不好：**
- 难以正确调用
- 参数顺序容易搞混
- 说明函数做了太多事
- 难以新增参数

**重构手法：**
- Introduce Parameter Object
- Preserve Whole Object
- Replace Parameter with Method Call
- Remove Flag Argument

**示例（重构前）：**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**示例（重构后）：**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### 数据泥团（Data Clumps）

**迹象：**
- 同样的 3 个以上字段反复一起出现
- 总是一起传递的参数
- 类里某些字段子集本属同一概念

**为何不好：**
- 重复的处理逻辑
- 缺少抽象
- 扩展更困难
- 暗示背后应有一个类

**重构手法：**
- Extract Class
- Introduce Parameter Object
- Preserve Whole Object

**示例：**
```javascript
// Data clump: (x, y, z) coordinates
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// Extract Point3D class
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## 面向对象误用（Object-Orientation Abusers）

表示对面向对象原则使用不完整或不当的坏味道。

### Switch 语句（Switch Statements）

**迹象：**
- 很长的 switch/case 或 if/else 链
- 多处出现相同的 switch
- 根据类型码分支
- 新增分支要在许多地方修改

**为何不好：**
- 违背开闭原则
- 改动会波及所有 switch 位置
- 难以扩展
- 常常说明缺少多态

**重构手法：**
- Replace Conditional with Polymorphism
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**示例（重构前）：**
```javascript
function calculatePay(employee) {
  switch (employee.type) {
    case 'hourly':
      return employee.hours * employee.rate;
    case 'salaried':
      return employee.salary / 12;
    case 'commissioned':
      return employee.sales * employee.commission;
  }
}
```

**示例（重构后）：**
```javascript
class HourlyEmployee {
  calculatePay() {
    return this.hours * this.rate;
  }
}

class SalariedEmployee {
  calculatePay() {
    return this.salary / 12;
  }
}
```

---

### 临时字段（Temporary Field）

**迹象：**
- 实例变量只在部分方法里使用
- 字段按条件设置
- 某些场景下初始化很复杂

**为何不好：**
- 容易困惑——字段存在但可能为 null
- 难以理解对象状态
- 说明条件逻辑被隐藏

**重构手法：**
- Extract Class
- Introduce Null Object
- Replace Temp Field with Local

---

### 被拒绝的遗赠（Refused Bequest）

**迹象：**
- 子类不使用继承来的方法/数据
- 子类重写后什么也不做
- 继承是为了复用代码，而不是 IS-A 关系

**为何不好：**
- 抽象错误
- 违背里氏替换原则
- 层次结构具有误导性

**重构手法：**
- Push Down Method/Field
- Replace Subclass with Delegate
- Replace Inheritance with Delegation

---

### 异曲同工的类（Alternative Classes with Different Interfaces）

**迹象：**
- 两个类做类似的事
- 同一概念用了不同的方法名
- 本可互换使用

**为何不好：**
- 实现重复
- 没有共同接口
- 难以在实现间切换

**重构手法：**
- Rename Method
- Move Method
- Extract Superclass
- Extract Interface

---

## 阻碍变更（Change Preventers）

使修改变困难的坏味道——改一处要连带改很多处。

### 发散式变化（Divergent Change）

**迹象：**
- 一个类因多种不同原因被修改
- 不同区域的改动都会动到同一个类
- 类是「上帝类」

**为何不好：**
- 违背单一职责
- 变更频率高
- 容易产生合并冲突

**重构手法：**
- Extract Class
- Extract Superclass
- Extract Subclass

**示例：**
`User` 类会因以下原因被修改：
- 认证相关变更
- 资料相关变更
- 计费相关变更
- 通知相关变更

→ 提炼出：`AuthService`、`ProfileService`、`BillingService`、`NotificationService`

---

### 霰弹式修改（Shotgun Surgery）

**迹象：**
- 一次改动要改很多个类
- 一个小功能要动 10 个以上文件
- 改动分散，难以找全

**为何不好：**
- 容易漏改
- 耦合度高
- 改动容易出错

**重构手法：**
- Move Method
- Move Field
- Inline Class

**识别：**
留意：增加一个字段就要改超过 5 个文件之类的情况。

---

### 平行继承体系（Parallel Inheritance Hierarchies）

**迹象：**
- 在一个层次结构中新建子类时，必须在另一个层次结构中也建子类
- 类名前缀成对出现（例如 `DatabaseOrder`、`DatabaseProduct`）

**为何不好：**
- 维护成本翻倍
- 两套层次结构相互耦合
- 容易只改一侧而忘记另一侧

**重构手法：**
- Move Method
- Move Field
- 消除其中一套层次结构

---

## 冗余（Dispensables）

本可去掉的多余部分。

### 注释（过多）（Comments (Excessive)）

**迹象：**
- 注释在解释代码在做什么
- 被注释掉的代码
- 永远留着的 TODO/FIXME
- 注释里的道歉式说明

**为何不好：**
- 注释会撒谎（与代码脱节）
- 代码应能自解释
- 死代码造成困惑

**重构手法：**
- Extract Method（用名字说明做什么）
- Rename（不靠注释也能说清楚）
- 删除注释掉的代码
- Introduce Assertion

**好注释 vs 坏注释：**
```javascript
// BAD: Explaining what
// Loop through users and check if active
for (const user of users) {
  if (user.status === 'active') { }
}

// GOOD: Explaining why
// Active users only - inactive are handled by cleanup job
const activeUsers = users.filter(u => u.isActive);
```

---

### 重复代码（Duplicate Code）

**迹象：**
- 相同代码出现在多处
- 仅有小差别的相似代码
- 复制粘贴模式

**为何不好：**
- 修 bug 要改多处
- 容易不一致
- 代码库臃肿

**重构手法：**
- Extract Method
- Extract Class
- Pull Up Method（在层次结构中）
- Form Template Method

**识别规则：**
重复出现 3 次及以上的代码应被提炼。

---

### 冗赘类（Lazy Class）

**迹象：**
- 类所做不足以支撑其存在
- 没有增加价值的包装层
- 过度设计的结果

**为何不好：**
- 维护负担
- 不必要的间接层
- 复杂度没有带来收益

**重构手法：**
- Inline Class
- Collapse Hierarchy

---

### 死代码（Dead Code）

**迹象：**
- 不可达代码
- 未使用的变量/方法/类
- 被注释掉的代码
- 位于永远不可能成立的条件后的代码

**为何不好：**
- 造成困惑
- 增加维护负担
- 拖慢理解速度

**重构手法：**
- Remove Dead Code
- Safe Delete

**识别：**
```bash
# 查找未使用的导出
# 查找未被引用的函数
# IDE 的「未使用」警告
```

---

### 夸夸其谈通用性（Speculative Generality）

**迹象：**
- 抽象类只有一个子类
- 标称「以后会用」却未使用的参数
- 只做转调的方法
- 为单一用例搭的「框架」

**为何不好：**
- 复杂度没有带来收益
- YAGNI（你不会需要它）
- 更难理解

**重构手法：**
- Collapse Hierarchy
- Inline Class
- Remove Parameter
- Rename Method

---

## 耦合过重（Couplers）

表示类之间耦合过强的坏味道。

### 依恋情结（Feature Envy）

**迹象：**
- 函数使用另一个类的数据比使用自身还多
- 大量调用另一个对象的 getter
- 数据与行为分离

**为何不好：**
- 行为放错了位置
- 封装不佳
- 难以维护

**重构手法：**
- Move Method
- Move Field
- Extract Method（再移动）

**示例（重构前）：**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // Uses customer data heavily
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**示例（重构后）：**
```javascript
class Customer {
  getDiscountedPriceFor(price) {
    if (this.loyaltyYears > 5) {
      return price * this.discountRate;
    }
    return price;
  }
}
```

---

### 狎昵关系（Inappropriate Intimacy）

**迹象：**
- 类之间访问对方的私有细节
- 双向引用
- 子类对父类知道得太多

**为何不好：**
- 高耦合
- 改动连锁反应
- 难以只改一侧

**重构手法：**
- Move Method
- Move Field
- Change Bidirectional to Unidirectional
- Extract Class
- Hide Delegate

---

### 消息链（Message Chains）

**迹象：**
- 很长的方法调用链：`a.getB().getC().getD().getValue()`
- 客户端依赖导航结构
- 「火车残骸」式代码

**为何不好：**
- 脆弱——链上任意一环变化都会破坏调用
- 违背得墨忒耳法则
- 与结构紧耦合

**重构手法：**
- Hide Delegate
- Extract Method
- Move Method

**示例：**
```javascript
// Bad: Message chain
const managerName = employee.getDepartment().getManager().getName();

// Better: Hide delegation
const managerName = employee.getManagerName();
```

---

### 中间人（Middle Man）

**迹象：**
- 类只做向另一类的转调
- 一半左右的方法是委托
- 没有附加价值

**为何不好：**
- 不必要的间接
- 维护负担
- 架构令人困惑

**重构手法：**
- Remove Middle Man
- Inline Method

---

## 坏味道严重程度指南

| 严重程度 | 说明 | 处理建议 |
|----------|------|----------|
| **Critical（严重）** | 阻碍开发、导致缺陷 | 立即处理 |
| **High（高）** | 维护负担明显 | 在当前迭代内处理 |
| **Medium（中）** | 明显但尚可承受 | 近期列入计划 |
| **Low（低）** | 轻微不便 | 有机会再改 |

---

## 快速排查清单

浏览代码时可用本清单自检：

- [ ] 是否有函数超过 30 行？
- [ ] 是否有类超过 300 行？
- [ ] 是否有参数超过 4 个的方法？
- [ ] 是否有重复的代码块？
- [ ] 是否有针对类型码的 switch/case？
- [ ] 是否有未使用代码？
- [ ] 是否有大量依赖其他类数据的方法？
- [ ] 是否有很长的方法调用链？
- [ ] 是否有在解释「做什么」而非「为什么」的注释？
- [ ] 是否有本应封装成对象的基本类型？

---

## 延伸阅读

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*
