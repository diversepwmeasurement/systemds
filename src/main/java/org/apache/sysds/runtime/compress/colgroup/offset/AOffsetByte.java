/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.sysds.runtime.compress.colgroup.offset;

public abstract class AOffsetByte extends AOffset implements ISliceOffset {

	private static final long serialVersionUID = -4716104973912491790L;
	protected static final int maxV = 255;

	protected final byte[] offsets;
	protected final int offsetToFirst;
	protected final int offsetToLast;

	protected AOffsetByte(byte[] offsets, int offsetToFirst, int offsetToLast) {
		this.offsets = offsets;
		this.offsetToFirst = offsetToFirst;
		this.offsetToLast = offsetToLast;
	}

	@Override
	public final int getOffsetToFirst() {
		return offsetToFirst;
	}

	@Override
	public final int getOffsetToLast() {
		return offsetToLast;
	}

	@Override
	public final int getLength() {
		return offsets.length;
	}
}
